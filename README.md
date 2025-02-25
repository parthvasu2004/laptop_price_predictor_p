💻 **Laptop Price Predictor**


Accurately Predict Laptop Prices Using Machine Learning


🔗 Repository: parthvasu2004/laptop_price_predictor_p


🚀 Overview


The Laptop Price Predictor is a machine learning-based web application designed to estimate the price of a laptop based on its specifications. It utilizes historical pricing data and a trained ML model to provide accurate predictions.


🛠️ Features


✔️ Predict Laptop Prices based on specifications like brand, RAM, processor, storage, and more.
✔️ Machine Learning Model trained on a dataset of laptop prices (laptop_data.csv).
✔️ Flask Web App for an easy-to-use interface.
✔️ Interactive UI for users to input specifications and get predictions instantly.
✔️ Live Deployment on Render for seamless access.


📂 Project Structure


laptop_price_predictor_p/
│── templates/          # HTML templates for web app  
│── app.py              # Flask web application  
│── df.pkl              # Preprocessed dataset  
│── laptop_data.csv     # Raw dataset with laptop specifications and prices  
│── pipe.pkl            # Trained ML model pipeline  
│── requirements.txt    # Python dependencies  
│── .gitignore          # Ignored files  
│── README.md           # Project documentation  


⚙️ Installation & Setup


1️⃣ Clone the Repository

git clone https://github.com/parthvasu2004/laptop_price_predictor_p.git
cd laptop_price_predictor_p


2️⃣ Create & Activate Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows


3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Run the Application

python app.py
Visit http://127.0.0.1:5000/ in your browser to access the web app.


🏆 Usage


1️⃣ Open the web application.
2️⃣ Enter laptop specifications (brand, processor, RAM, storage, GPU, etc.).
3️⃣ Click "Predict" to get the estimated price.


🎯 Model & Training


Dataset: Uses laptop_data.csv, which contains laptop specifications and their prices.
Algorithm: Trained using Machine Learning Regression Models.
Features Used:
Brand
Processor Type
RAM Size
Storage Type (HDD/SSD)
Graphics Card
Display Size


🔗 Live Deployment


The application is deployed on Render for public access. Click here: https://laptop-price-predictor-mhp.onrender.com


🤝 Contribution


Contributions are welcome! Feel free to fork this repository, create feature branches, and submit pull requests.


📜 License


This project is licensed under the MIT License – free to use and modify.


📬 Contact
👤 Parth Pandey
📧 parthvasu2004@gmail.com
🔗 [linkedin.com/in/parth-pandey-3442a9256](https://www.linkedin.com/in/parth-pandey-3442a9256/)
