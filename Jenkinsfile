pipeline {
    agent any

    stages {

        stage('PR Check') {
            when {
                expression { env.CHANGE_ID != null }
            }
            steps {{
                echo "----------------------------------"
                echo "Hello World 👋"
                echo "PR detected successfully!"
                echo "PR Number      : ${env.CHANGE_ID}"
                echo "Source Branch  : ${env.CHANGE_BRANCH}"
                echo "Target Branch  : ${env.CHANGE_TARGET}"
                echo "----------------------------------"
            }
        }

        stage('Build') {
            when {
                expression { env.CHANGE_ID != null }
            }
            steps {
                sh '''
                echo "Running sample build step..."
                echo "Build SUCCESS for PR #${CHANGE_ID}"
                '''
            }
        }
    }

    post {
        success {
            echo "PR pipeline completed successfully ✅"
        }
        failure {
            echo "PR pipeline failed ❌"
        }
        always {
            echo "Pipeline finished."
        }
    }
}
