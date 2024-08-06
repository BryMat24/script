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
        stage('Check Migration') {
            steps {
                // get target version input 
                script {
                    def targetVersion = input(
                        id: 'userInput', 
                        message: 'Enter the following value:',
                        parameters: [
                            string(
                                defaultValue: 'None',
                                description: 'Migration version',
                                name: 'target_version'
                            )
                        ]
                    )

                    echo "Target migration version: ${targetVersion}"

                    // run python script
                    sh "python3 -u check_migration.py --db_uri \"${env.DB_URI}\" --target_version \"${targetVersion}\""
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
