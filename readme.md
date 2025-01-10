# Social Media Post Analysis Flow 🌐📊

This repository provides a Python-based flow for analyzing **social media posts**. The flow utilizes LangFlow and AstraDB to extract insights and compare the performance of different post types (e.g., reels, images, carousels).

The project is designed for **data-driven decision-making**, enabling users to identify trends and actionable insights from social media post data.

---

## 🚀 Features

- **Customizable AI Flow**: Analyze and compare post types like reels, carousels, and images.
- **Data Handling**: Extract metrics such as:
  - Average likes
  - Engagement rates (likes per view)
  - Comments, shares, and more.
- **Actionable Insights**: Generates user-friendly, quantified observations to guide social media strategies.
- **Plug-and-Play Design**: Seamlessly integrates LangFlow and AstraDB with tweakable parameters.

---

## 🛠️ Technologies Used

- **LangFlow**: To power the flow of social media analysis.
- **AstraDB**: As the database to store and fetch social media data.
- **OpenAI GPT**: To generate insights with intuitive metrics and comparisons.
- **Python**: For flow orchestration and customization.

---

## 🖥️ Setup and Installation

### Prerequisites

- AstraDB account and application token.

### Installation Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/UditJain2622004/supermind-pre-hackathon-task.git
   cd supermind-pre-hackathon-task
   ```

2. Install required dependencies:

   ```bash
   pip install requests
   ```

3. Set your environment variables:
   - Replace `<YOUR_APPLICATION_TOKEN>` with your **AstraDB Application Token** in the script.
   - Update other placeholders like `LANGFLOW_ID`, `FLOW_ID`, and `BASE_API_URL` with your specific values.

---

## 🧑‍💻 Usage

Run the script with a message and optional tweaks. Provide a comma separated list of types of posts you want to analyze.

### Example:

```bash
python final.py "reel, image, video"
```

### Expected Output

- A **tabular summary** of post metrics (e.g., likes, engagement rate, comments, shares).
- Simple, concise **insights** (e.g., "Reels receive 3x more comments than images.").

---

## 🛠 Flow Components

### 1️⃣ **Agent**:

- Powered by OpenAI GPT models (e.g., `gpt-4o`).
- Designed to extract actionable insights with clarity and precision.

### 2️⃣ **Database Integration**:

- **AstraDB Tool**: Fetches and filters social media post data based on post type.

### 3️⃣ **Custom Python Analysis**:

- Leverages a Python REPL tool for custom data analysis.

---

## 📊 Example Outputs

### Sample Insights:

- **Tabular Metrics**:
  | Post Type | Avg Likes | Engagement Rate | Avg Comments |
  |-----------|-----------|-----------------|--------------|
  | Reels | 1,000 | 12% | 300 |
  | Images | 500 | 8% | 50 |

- **Insights**:
  - "Reels generate 2x more engagement compared to images."
  - "Videos have 3x the average views of carousel posts."
  - "Images receive only 5% of the engagement that reels do."

---

## 🔧 Configuration

### Tweakable Parameters:

Customize the flow behavior via the `TWEAKS` dictionary:

- **ChatOutput Configuration**:
  - Update color schemes, sender details, and templates.
- **Agent Settings**:
  - Change models (e.g., `gpt-3.5-turbo`, `gpt-4`).
  - Update system prompts for domain-specific analysis.

---
