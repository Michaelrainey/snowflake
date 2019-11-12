pipeline {
  options {
    timeout(time: 1, unit: 'HOURS')
  }
  agent {
    docker {
      args "-u root -v /var/run/docker.sock:/var/run/docker.sock --entrypoint=''"
      image 'hashmapinc/sqitch:jenkins'
    }
  }
  stages {
    stage('Moving .snowsql to workspace and replacing snowsql in /bin') {
      steps {
        sh '''rm /bin/snowsql 
        mv /var/snowsql /bin/
        mv /var/.snowsql ./
        '''
      }
    }
    stage('Deploy changes') {
      steps {
        withCredentials(bindings: [usernamePassword(credentialsId: 'snowflake_creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh '''
            sqitch deploy "db:snowflake://$USERNAME:$PASSWORD@aws_cas2.snowflakecomputing.com/flipr?Driver=Snowflake;warehouse=mraineywh"
            '''
        }
      }
    }
    stage('Verify changes') {
      steps {
        withCredentials(bindings: [usernamePassword(credentialsId: 'snowflake_creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh '''
            sqitch verify "db:snowflake://$USERNAME:$PASSWORD@aws_cas2.snowflakecomputing.com/flipr?Driver=Snowflake;warehouse=mraineywh"
            '''
        }
      }
    }
  }
  post {
    always {
      sh 'chmod -R 777 .'
    }
  }
}
