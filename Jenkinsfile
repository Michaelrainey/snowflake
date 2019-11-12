pipeline {
  agent {
    docker {
      args '-u root -v /var/run/docker.sock:/var/run/docker.sock --entrypoint=\'\''
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

  }
  environment {
    time = '1'
    unit = 'HOURS'
  }
}