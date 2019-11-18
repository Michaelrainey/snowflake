pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('Deploy changes') {
      steps {
        withCredentials(bindings: [usernamePassword(credentialsId: 'snowflake_creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh '''
sqitch deploy "db:snowflake://mrainey@aws_cas2.snowflakecomputing.com/mrainey?Driver=Snowflake;warehouse=mraineywh"            '''
        }

      }
    }

    stage('Verify changes') {
      steps {
        withCredentials(bindings: [usernamePassword(credentialsId: 'snowflake_creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh '''
sqitch verify "db:snowflake://mrainey@aws_cas2.snowflakecomputing.com/mrainey?Driver=Snowflake;warehouse=mraineywh"            '''
        }

      }
    }

  }
  post {
    always {
      sh 'chmod -R 777 .'
    }

  }
  options {
    timeout(time: 1, unit: 'HOURS')
  }
}
