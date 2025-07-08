# 🛡️ Anomaly Detection in Cybersecurity

This is my **Final Year Project** focused on applying machine learning and clustering techniques to detect anomalies in network traffic and system behavior — helping to identify potential cybersecurity threats and intrusions.

---

## 🎯 Project Objective

To build an intelligent system that detects unusual patterns in cybersecurity data, such as abnormal login attempts, unauthorized access, or suspicious network behavior — helping organizations improve threat detection and response.

---

## 📁 Dataset

- ✅ Format: CSV
- ✅ Source: Synthetic or real network log data
- ✅ Features: IP address, protocol, duration, bytes transferred, flags, etc.
- ✅ Label: Normal or Anomaly (in some versions)

> *Note: If using public datasets like NSL-KDD, CICIDS, or custom logs, mention them here.*

---

## 🧠 Techniques Used

- **Unsupervised Learning**:
  - DBSCAN (Density-Based Clustering)
  - PCA for dimensionality reduction

- **Supervised Learning** (optional):
  - Decision Trees
  - Random Forest

- **Preprocessing**:
  - Feature scaling
  - Label encoding
  - Handling nulls/outliers

---

## 🛠️ Tech Stack

| Tool / Library        | Purpose                      |
|-----------------------|------------------------------|
| Python                | Core programming             |
| Pandas, NumPy         | Data processing              |
| Scikit-learn          | ML models & metrics          |
| Matplotlib, Seaborn   | Visualization                |
| Git, GitHub           | Version control              |
| (Optional) Django/Flask | Web deployment (if any)     |

---

## 📊 Visualizations

- PCA Scatter Plots to visualize clusters
- DBSCAN clustering result (with noise detection)
- Pie chart of anomaly vs normal traffic
- Parallel coordinates for high-dimensional insight

---

## 🧪 Results

- ✔️ Detected multiple outliers with DBSCAN
- ✔️ Achieved silhouette score of ~`X.XX` (edit with your best score)
- ✔️ Grouped data into meaningful clusters (e.g., benign traffic, suspicious access)

---

## 🚀 Future Improvements

- Integrate real-time anomaly detection
- Use deep learning models like Autoencoders or LSTM
- Deploy with Flask/Django for live monitoring dashboards

---

## 👨‍💻 Author

**Naveenkumar**  
Final Year B.Tech (Information Technology)  
Dhanalakshmi Srinivasan College of Engineering and Technology  
GitHub: [@Naveen220104](https://github.com/Naveen220104)

---

## 📎 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/Naveen220104/Anomaly-Detection.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the notebook or script
python main.py
