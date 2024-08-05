pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
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
                    def target_version
                    def db_uri

                    // Get the input
                    def userInput = input(
                        id: 'userInput', 
                        message: 'Enter the following values:',
                        parameters: [
                            string(
                                defaultValue: 'None',
                                description: 'Target migration version',
                                name: 'target_version'
                            ),
                            string(
                                defaultValue: 'None',
                                description: 'Database URI',
                                name: 'db_uri'
                            )
                        ]
                    )

                    // Save to variables. Default to empty string if not found.
                    target_version = userInput.target_version ?: ''
                    db_uri = userInput.db_uri ?: ''

                    echo "Target migration version: ${target_version}"
                    echo "Database URI: ${db_uri}"
                }
            }
        }
    }

    post {
        success {
            // Example of a success message. Replace with your Slack notification step.
            echo 'Success: Notify Slack here.'
        }
        failure {
            // Example of a failure message. Replace with your Slack notification step.
            echo 'Failure: Notify Slack here.'
        }
    }
}
