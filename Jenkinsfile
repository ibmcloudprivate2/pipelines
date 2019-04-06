pipeline {
  agent any
  stages {
    stage('backupfiles') {
      steps {
        sh 'echo backupfiles '
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