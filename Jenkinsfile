pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
        }
    }

    environment {
        DB_URI = 'postgresql://postgres:postgrespw@host.docker.internal:5432/kabam_db'
    }

    stages {
        stage('Checkout scm') {
            steps {
                git credentialsId: 'github-credential', url: 'https://github.com/BryMat24/script.git', branch: 'main'
            }
        }

        stage('Test Database Connection') {
            steps {
                script {
                    def dbUri = env.DB_URI
                    def dbType = 'postgresql' // Change according to your database

                    echo "Testing connection to the database: ${dbUri}"

                    try {
                        // Test PostgreSQL connection
                        if (dbType == 'postgresql') {
                            sh """
                                pg_isready -d ${dbUri}
                            """
                        } 
                        // Add other database types as needed
                        else {
                            error "Unsupported database type: ${dbType}"
                        }
                    } catch (Exception e) {
                        echo "Database connection failed: ${e.message}"
                        currentBuild.result = 'FAILURE'
                    }
                }
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
                            )
                        ]
                    )

                    // Save to variables. Default to empty string if not found.
                    target_version = userInput.target_version ?: ''
                    echo "Target migration version: ${target_version}"
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
