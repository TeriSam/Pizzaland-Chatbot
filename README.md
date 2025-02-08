# Pizzaland-Chatbot
A Rasa-based chatbot for ordering pizza (Uni assignment)
## 📌 Project Overview
This project is a **Task-Oriented Dialog System (TODS) chatbot** built using **Rasa Open Source**. It allows users to order, modify, track, and cancel pizzas through a conversational AI interface. The chatbot also integrates **real-time weather data** and provides **simulated store hours**.

## 📂 Project Structure
```
rasaproject/
├── actions.py         # Custom actions for order handling & API integration
├── config.yml         # Rasa pipeline configuration
├── data/
│   ├── nlu.yml       # Training examples for intents
│   ├── stories.yml   # Conversation flows
│   ├── rules.yml     # Rules for intent handling
├── domain.yml        # Defines intents, entities, slots, responses, and actions
├── endpoints.yml     # Action server configuration
├── models/           # Trained Rasa models
├── README.md         # Project documentation (this file)
└── presentation.pdf  # Final submission slides
```

## 🚀 Features
- **Order Pizza**: Users can specify pizza type and size.
- **Modify Order**: Users can add/remove toppings.
- **Track Order**: Provides order status updates.
- **Cancel Order**: Allows users to cancel an existing order.
- **Store Hours Information**: Provides **simulated** store opening/closing hours.
- **Weather-Based Delivery Estimates**: Uses **real-time weather data** to adjust estimated delivery time.
- **Robust Error Handling**: Handles unexpected inputs gracefully.

## 🔧 Installation & Setup
###1️⃣ Install Dependencies
Ensure you have **Python 3.8+** and Rasa installed:
```bash
pip install rasa
pip install rasa-sdk
pip install requests
```

### 2️⃣ Train the Model
```bash
rasa train
```

### 3️⃣ Run the Action Server
```bash
rasa run actions
```

### 4️⃣ Start the Chatbot
```bash
rasa shell
```

## 📑 Usage Guide
Try the following test phrases:
- **Ordering Pizza:**
  - "I want to order a pizza"
  - "Can I get a large Pepperoni pizza?"
- **Modifying an Order:**
  - "I want to change my order"
  - "Can I add mushrooms?"
- **Tracking an Order:**
  - "Where is my pizza?"
- **Cancelling an Order:**
  - "I want to cancel my order"
- **Checking Store Hours:**
  - "What time do you open?"
- **Checking Weather-Based Delivery Estimates:**
  - "How long will my order take?"

## 🌍 Data Integration
1️⃣ **Simulated Store Hours**:  
   - The chatbot provides **hardcoded store hours**:  
     _"Our store is open from 10:00 AM to 11:00 PM every day."_

2️⃣ **Weather API Integration**:  
   - Uses **OpenWeatherMap API** to fetch live weather and adjust estimated delivery time.  
   - Example response:  
     _"The current weather in Athens is clear sky with a temperature of 18°C."_

## 🛠 Customization
- **Modify `nlu.yml`** to add more training phrases.
- **Edit `actions.py`** to adjust business logic.
- **Deploy on Telegram, Twilio, or Webchat** for real-world usage.

## 📌 Challenges Faced & Solutions
### **Challenge: Handling User Input Variations**
- **Solution:** Improved training examples in `nlu.yml` to better recognize variations like "Can I get a pizza?" vs. "I want to order a pizza."

### **Challenge: Handling API Failures**
- **Solution:** Implemented **try-except** blocks to provide default responses if APIs fail.

### **Challenge: Preventing Duplicate Prompts**
- **Solution:** Adjusted `stories.yml` and `actions.py` to ensure the bot doesn't repeatedly ask for missing details.

## 📑 Submission Files
- ✅ **GitHub Repository** (includes all source files & trained model)
- ✅ **Presentation Slides (`presentation.pdf`)**
- ✅ **Final Chatbot Demo Video (if required)**

## 📞 Contact & Support
For questions or issues, reach out to **[Teri Samari]** at **[efterpi.sam@gmail.com]**.

---

