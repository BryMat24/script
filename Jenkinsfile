pipeline {
    agent any

    environment {
        DB_URI = 'postgresql://postgres:postgrespw@host.docker.internal:5432/kabam_db'
    }

    stages {
        stage('Checkout scm') {
            steps {
                git credentialsId: 'github-credential', url: 'https://github.com/BryMat24/script.git', branch: 'main'
            }
        }

        stage('Check Migration') {
            steps {
                script {
                    // Prompt user for input
                    def userInput = input(
                        id: 'userInput', 
                        message: 'Enter the following values:',
                        parameters: [
                            string(
                                defaultValue: 'None',
                                description: 'Target migration version',
                                name: 'target_version'
                            )
                        ]
                    )

                    // Access the input value
                    def targetVersion = userInput['target_version']
                    echo "Target Migration Version: ${targetVersion}"
                }
            }
        }
    }

    post {
        success {
            // Notify on success
            echo 'Success: Notify Slack here.'
        }
        failure {
            // Notify on failure
            echo 'Failure: Notify Slack here.'
        }
    }
}
