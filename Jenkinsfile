// pipeline = Jenkins ko batata hai ki ye Declarative Pipeline hai
pipeline {

    // agent any = pipeline kisi available Jenkins agent par run hogi
    // Tumhare case mein Jenkins agent tumhari Ubuntu VM hai
    agent any

    // environment = pipeline ke liye reusable variables define karte hain
    environment {

        // Docker image ka complete repository name
        IMAGE_NAME = 'rootmanish/jenkins-devsecops'

        // Docker image ka tag/version
        IMAGE_TAG = 'v1'
    }

    // stages = pipeline ke saare major steps yahan define hote hain
    stages {

        // ============================================================
        // STAGE 1: CHECKOUT
        // ============================================================

        // stage() pipeline mein ek logical step/group banata hai
        stage('Checkout') {

            // steps = is stage ke andar actual commands/actions
            steps {

                // Jenkins GitHub se source code checkout karega
                // SCM = Jenkins job mein configured Git repository
                checkout scm
            }
        }


        // ============================================================
        // STAGE 2: TRIVY FILESYSTEM SCAN
        // ============================================================

        // Source code aur dependency files ko security scan karna
        stage('Trivy Filesystem Scan') {

            // Is stage ke commands
            steps {

                // sh = Ubuntu/Linux shell command execute karo
                // trivy fs = filesystem scan
                // --severity HIGH,CRITICAL = sirf high/critical vulnerabilities show karo
                // . = current Jenkins workspace
                sh 'trivy fs --severity HIGH,CRITICAL .'
            }
        }


        // ============================================================
        // STAGE 3: DOCKER BUILD
        // ============================================================

        // Application ka Docker image create karna
        stage('Docker Build') {

            // Docker build command execute karna
            steps {

                // Dockerfile ko use karke image build hogi
                // -t = image ko name aur tag dena
                // ${IMAGE_NAME} = rootmanish/jenkins-devsecops
                // ${IMAGE_TAG} = v1
                // . = current workspace ko build context banana
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }


        // ============================================================
        // STAGE 4: TRIVY IMAGE SCAN
        // ============================================================

        // Final Docker image ko security scan karna
        stage('Trivy Image Scan') {

            // Is stage ke commands
            steps {

                // Trivy final Docker image ko scan karega
                // Filesystem scan aur Image scan alag hain
                sh 'trivy image --severity HIGH,CRITICAL ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }


        // ============================================================
        // STAGE 5: DOCKER HUB PUSH
        // ============================================================

        // Successfully built aur scanned image ko Docker Hub par upload karna
        stage('Docker Hub Push') {

            // Is stage ke commands
            steps {

                        // Username ko temporary environment variable mein rakho
                        usernameVariable: 'DOCKER_USERNAME',

                        // Password/token ko temporary environment variable mein rakho
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {

                    // Multiple Linux shell commands execute karne ke liye '''
                    sh '''

                        # Docker Hub mein login
                        # Password/token command line argument mein nahi diya ja raha
                        # --password-stdin securely password/token read karta hai
                        echo "$DOCKER_PASSWORD" | docker login \
                            -u "$DOCKER_USERNAME" \
                            --password-stdin

                        # Docker image ko Docker Hub par push karo
                        # Result:
                        # rootmanish/jenkins-devsecops:v1
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}

                        # Kaam complete hone ke baad Docker Hub se logout
                        docker logout
                    '''
                }
            }
        }
    }
}
                        // Jenkins credential ka ID
                        credentialsId: 'dockerhub-creds',

                // Jenkins Credentials Store se credentials securely read karo
                    usernamePassword(
                // credentialsId = Jenkins mein banaya hua credential
                withCredentials([
                    // Username + password/token type credential

