pipeline {
  agent any
  parameters {
    choice(name: 'env',
      choices: 'dev\ntest\nprod\ndr',
      description: 'What door do you choose?')
    string(name: 'host',
      description: 'Specify remote host IP')
    string(name: 'user',
      defaultValue: 'user',
      description: 'Do the funky chicken!')
    password(name: 'password',
      description: 'password to remote host')
  }  
  stages {
    stage('backupfiles') {
      steps {
        sh 'echo backupfiles '
        sh "echo env: ${params.env}"
        sh "echo host: ${params.host}"
        sh "echo user: ${params.user}"
        sh "echo pw: ${params.password}"
      }
    }
    stage('copyfiles') {
      steps {
        sh 'echo copyfiles'
      }
    }
    stage('backupdb') {
      steps {
        sh 'echo backupdb'
      }
    }
    stage('updatedb') {
      steps {
        sh 'echo updatedb'
      }
    }
    stage('validate-page') {
      parallel {
        stage('validate-page') {
          steps {
            sh 'echo validate-page'
          }
        }
        stage('validate-sitemap') {
          steps {
            sh 'echo validate-sitemap'
          }
        }
        stage('validate-report') {
          steps {
            sh 'echo validate-report'
          }
        }
      }
    }
    stage('') {
      steps {
        sh 'echo pipeline-completed'
      }
    }
  }
}