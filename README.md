
### SmartHarvest---The-Crop-Predictor  
This project leverages advanced machine learning (ML) techniques to optimize crop yield predictions, helping farmers manage limited resources effectively. By analyzing soil nutrients, environmental factors, and weather conditions, the system aids in agricultural decision-making.  

---

#### Project Description  
**SmartHarvest** is designed to address critical challenges in agriculture by providing accurate crop predictions using a dataset of 2,200 entries across various crops. The project analyzes parameters such as soil nutrients (N, P, K), temperature, humidity, rainfall, and soil pH. It incorporates multiple machine learning models to forecast crop suitability and improve resource management.  

This tool is instrumental in modernizing agriculture, reducing resource waste, and enhancing food security. By combining data-driven insights and precision agriculture, the system empowers farmers to make informed decisions and boost productivity.  

---

#### Features  
- **Accurate Predictions**: Leverages ML algorithms to predict suitable crops based on input parameters.  
- **Multi-Model Approach**: Utilizes and compares multiple algorithms for robust performance.  
- **Scalable and Adaptable**: Easily integrates with modern agricultural practices and tools.  

---

#### Model Selection  
Various models were evaluated on accuracy, precision, recall, and F1-score to identify the most effective approach:  
- **Naive Bayes**: Achieved the highest accuracy of 99.55%.  .    
- **Decision Trees**: Achieved 98.86% accuracy.  
- **K-Nearest Neighbors (KNN)**: 97.05% accuracy.  
- **Support Vector Machines (SVM)**: 96.14% accuracy.  
- **Logistic Regression**: 94.55% accuracy.  

---

#### Steps for Prediction  
1. **Input Data**: Enter environmental and soil parameters.  
2. **Run Prediction**: Select a preferred model for crop prediction.  
3. **View Results**: Receive a detailed output with crop recommendations and analysis.  

---

#### Dependencies  
- Python (3.9.5)  
- Libraries: Scikit-learn, NumPy, Pandas, Matplotlib  

---

#### Installation  
Clone the repository:  
```bash
git clone <repository-url>
```  
Run the application:  
```bash
python app.py
```  
Access the application via a web browser at `http://127.0.0.1:5000`.  

---

#### Conclusion  
SmartHarvest demonstrates how machine learning can revolutionize agriculture by offering precise, data-driven insights for crop planning and resource management. The system's high accuracy and adaptability highlight its potential to modernize farming practices and tackle challenges like food security and environmental sustainability.  

Future enhancements could include expanding the dataset, incorporating real-time weather data, and integrating IoT-based sensors for improved predictions.  

---

#### About the Developer  
This project is developed by **Abhishek Kushwaha**.  
- **LinkedIn**: [Abhishek Kushwaha](https://www.linkedin.com/in/abhishek10027)  
- **GitHub**: [abhishek10027](https://github.com/abhishek10027)  

