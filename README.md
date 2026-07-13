# 🛡️ Network Security Phishing Detection

An end-to-end **Machine Learning & MLOps** project for detecting phishing websites using network traffic and URL-based features. This project demonstrates a complete production-ready workflow including **ETL Pipelines, Data Validation, Feature Engineering, Model Training, DagsHub MLflow Experiment Tracking, Docker Containerization, GitHub Actions CI/CD, FastAPI Deployment, and AWS Cloud Deployment.**

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-orange?logo=scikitlearn)
![MLflow](https://img.shields.io/badge/MLflow-0194E2)
![DagsHub](https://img.shields.io/badge/DagsHub-MLflow%20Tracking-0A66C2)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?logo=mongodb)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=githubactions)
![AWS EC2](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws)
![Amazon ECR](https://img.shields.io/badge/AWS-ECR-FF9900?logo=amazonaws)
![Amazon S3](https://img.shields.io/badge/AWS-S3-569A31?logo=amazons3&logoColor=white)


---

# ✨ Features

- End-to-End ETL Pipeline
- Production-Ready MLOps Pipeline
- Modular Object-Oriented Architecture
- Automated Data Validation
- Feature Engineering Pipeline
- Hyperparameter Tuning
- Automatic Best Model Selection
- DagsHub MLflow Experiment Tracking
- CSV-Based Prediction Pipeline
- FastAPI REST API
- Dockerized Deployment
- GitHub Actions CI/CD
- Amazon S3 Artifact & Model Storage
- Amazon ECR & EC2 Deployment
- MongoDB Atlas Integration
- Logging & Exception Handling


# 📸 Project Screenshots

### FastAPI Swagger UI

> *(Add Screenshot Here)*

### Project Folder Structure

> *(Add Screenshot Here)*

### DagsHub MLflow Tracking

> *(Add Screenshot Here)*

### GitHub Actions CI/CD Pipeline

> *(Add Screenshot Here)*

### AWS EC2 Deployment

> *(Add Screenshot Here)*

---

# 🏗️ Project Architecture

```text
MongoDB Atlas
      │
      ▼
Data Ingestion
      │
      ▼
Data Validation
      │
      ▼
Data Transformation
      │
      ▼
Feature Engineering
      │
      ▼
Model Training
      │
      ▼
Model Evaluation
      │
      ▼
DagsHub MLflow Tracking
      │
      ▼
Serialized Artifacts
      │
      ▼
Amazon S3 
      │
      ▼
FastAPI REST API
      │
      ▼
Docker Container
      │
      ▼
Amazon ECR
      │
      ▼
Amazon EC2
```

---

# 📁 Project Structure

```text
Network-Security/
│
├── .github/
│   └── workflows/
│       └── main.yml                                # GitHub Actions CI/CD pipeline
│
├── data_schema/
│   └── schema.yaml                                 # Dataset validation schema
│
├── Network_Data/
│   └── phishingData.csv                            # Raw phishing dataset
│
├── final_model/
│   ├── model.pkl                                   # Trained machine learning model
│   └── preprocessor.pkl                            # Data preprocessing pipeline
│
├── networksecurity/
│   ├── cloud/
│   │   └── s3_syncer.py                            # AWS S3 upload/download operations
│   │
│   ├── components/
│   │   ├── data_ingestion.py                       # Data ingestion module
│   │   ├── data_validation.py                      # Data validation module
│   │   ├── data_transformation.py                  # Feature engineering & preprocessing
│   │   └── model_trainer.py                        # Model training module
│   │
│   ├── constant/
│   │   └── training_pipeline/                      # Training pipeline constants
│   │
│   ├── entity/
│   │   ├── config_entity.py                        # Configuration entities
│   │   └── artifact_entity.py                      # Pipeline artifact entities
│   │
│   ├── exception/
│   │   └── exception.py                            # Custom exception handling
│   │
│   ├── logging/
│   │   └── logger.py                               # Logging configuration
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py                    # End-to-end training pipeline
│   │
│   └── utils/
│       ├── main_utils/
│       │   └── utils.py                            # Common utility functions
│       │
│       └── ml_utils/
│           ├── metric/
│           │   └── classification_metric.py        # Model evaluation metrics
│           │
│           └── model/
│               └── estimator.py                    # Model loading & prediction
│
├── prediction_output/
│   └── output.csv                                  # Batch prediction results
│
├── templates/
│   └── table.html                                  # HTML template for FastAPI
│
├── valid_data/
│   └── test.csv                                    # Sample input data
│
├── app.py                                          # FastAPI application entry point
├── push_data.py                                    # Upload dataset to MongoDB
├── test_mongodb.py                                 # MongoDB connection testing
├── Dockerfile                                      # Docker container configuration
├── requirements.txt                                # Project dependencies
├── setup.py                                        # Python package setup
├── README.md                                       # Project documentation
├── .env                                            # Environment variables
└── .gitignore                                      # Git ignored files
```


# 🔄 ETL Pipeline

## 📥 Extract

- MongoDB Atlas
- Automated Data Collection
- Batch Data Loading

## 🔄 Transform

- Data Cleaning
- Schema Validation
- Missing Value Handling
- Feature Engineering
- Feature Encoding
- Feature Scaling
- Data Preprocessing Pipeline

## 📤 Load

- NumPy Arrays
- Serialized Model Artifacts
- Preprocessing Pipeline
- Amazon S3 Model & Artifact Storage
- Prediction Outputs


# ⚙️ Machine Learning Pipeline

## Data Ingestion

- MongoDB Atlas Integration
- Data Extraction
- Train-Test Split
- Artifact Generation

## Data Validation

- Schema Validation
- Column Validation
- Data Drift Detection
- Missing Value Checks

## Data Transformation

- Feature Engineering
- Data Preprocessing
- Pipeline Creation
- Object Serialization

## Model Training

- Hyperparameter Tuning
- Multiple Model Comparison
- Automatic Best Model Selection
- Model Serialization

## Model Evaluation

- Precision
- Recall
- F1-Score
- Performance Comparison

## Prediction

- CSV Upload
- Data Preprocessing
- Model Inference
- Prediction Export

---

# 🤖 Machine Learning Models

- Random Forest Classifier
- Gradient Boosting Classifier
- AdaBoost Classifier
- Decision Tree Classifier
- Logistic Regression

Multiple machine learning algorithms are trained and compared using hyperparameter tuning. The pipeline automatically selects the best-performing model based on evaluation metrics.


# ☁️ CI/CD & Deployment

```text
GitHub Repository
        │
        ▼
GitHub Actions
        │
        ▼
Docker Image Build
        │
        ▼
Amazon Elastic Container Registry (ECR)
        │
        ▼
Amazon EC2 Instance
        │
        ▼
FastAPI REST API
```


# 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| **Language** | Python |
| **Machine Learning** | Scikit-learn, NumPy, Pandas |
| **Backend** | FastAPI |
| **Database** | MongoDB Atlas |
| **Experiment Tracking** | MLflow + DagsHub|
| **Containerization** | Docker |
| **CI/CD** | GitHub Actions |
| **Cloud** | Amazon EC2, Amazon ECR, Amazon S3 |
| **Utilities** | PyYAML, Dill, Certifi, Python-dotenv |

---

# 📈 Future Enhancements

- Kubernetes Deployment
- Model Drift Detection
- Automated Model Retraining
- Prometheus & Grafana Monitoring
- Real-Time Prediction API

---

## 👨‍💻 Author

Aryan Jaiswal

Computer Science Engineering Student

Madan Mohan Malaviya University of Technology

LinkedIn • GitHub