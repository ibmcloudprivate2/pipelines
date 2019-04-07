pipeline {
  agent any
  parameters {
    choice(name: 'env',
      choices: 'dry-run\ndev\ntest\nprod\ndr',
      defaultValue: 'dry-run',
      description: 'target env:')
    string(name: 'host',
      description: 'remote host IP')
    string(name: 'user',
      defaultValue: 'user',
      description: 'remote host user')
    password(name: 'password',
      description: 'remote host password')
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