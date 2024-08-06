pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    } 

    environment {
        DB_URI = credentials('329ed325-d7ad-4273-aa19-69fab85790bc')
    }

    stages {
        stage('Checkout scm') {
            steps {
                git credentialsId: 'github-credential', url: 'https://github.com/BryMat24/migration-script.git', branch: 'main'
            }
        }

        stage('Check Migration') {
            steps {
                script {
                    def target_version

                    // Get the input
                    def userInput = input(
                        id: 'userInput', 
                        message: 'Enter the following value:',
                        parameters: [
                            string(
                                defaultValue: 'None',
                                description: 'Target migration version',
                                name: 'target_version'
                            )
                        ]
                    )

                    // Save to variable. Default to empty string if not found.
                    target_version = userInput.target_version ?: ''

                    echo "Target migration version: ${target_version}"
                    echo "Database URI: ${env.DB_URI}"

                    // run python script
                    sh "python3 -u check_migration.py --db_uri \"${env.DB_URI}\" --target_version \"${target_version}\""
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
