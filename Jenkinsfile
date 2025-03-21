pipeline {
    agent any

    environment {
        GITHUB_TOKEN = credentials('github-token')  // GitHub token for authentication
        SSH_KEY = credentials('ssh-key')            // SSH key for deployment
        APP_DIR = 'devops-project/python-app'                      // Directory containing the Flask app
        STAGING_SERVER = 'ec2-user@3.83.174.167'      // Staging server details
        DEPLOY_PATH = '/home/ec2-user/devops-project/python-app/'                // Deployment path on the server
    }

    stages {
        // Stage 1: Checkout the code from GitHub
        stage('Checkout') {
            steps {
                git branch: 'main', url: "https://${GITHUB_TOKEN}@github.com/your-username/devops-project.git"
            }
        }

        // Stage 2: Build the application
        stage('Build') {
            steps {
                sh '''
                    echo "Building the application..."
                    cd ${APP_DIR}
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        // Stage 3: Run unit tests
        stage('Test') {
            steps {
                sh '''
                    echo "Running unit tests..."
                    cd ${APP_DIR}
                    python -m unittest test_app.py || exit 1
                '''
            }
        }

        // Stage 4: Deploy the application to the staging server
        stage('Deploy') {
            steps {
                sshagent(credentials: ['ssh-key']) {
                    sh '''
                        echo "Deploying the application..."
                        cd ${APP_DIR}
                        scp -r . ${STAGING_SERVER}:${DEPLOY_PATH} || { echo "Deployment failed!"; exit 1; }
                        ssh ${STAGING_SERVER} "cd ${DEPLOY_PATH} && python app.py" || { echo "Application start failed!"; exit 1; }
                    '''
                }
            }
        }
    }

    // Post-build actions (notifications)
    post {
        success {
            slackSend channel: '#devops', message: 'Pipeline succeeded!'
        }
        failure {
            slackSend channel: '#devops', message: 'Pipeline failed!'
        }
    }
}
