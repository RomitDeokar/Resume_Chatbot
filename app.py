import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import time

# Set page config
st.set_page_config(
    page_title="Romit Deokar - Resume",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define some colors
primary_color = "#2E4057"
secondary_color = "#048BA8"
accent_color = "#99C24D"

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E4057;
        font-weight: 800;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #048BA8;
        font-weight: 600;
    }
    .section-header {
        font-size: 1.3rem;
        color: #2E4057;
        font-weight: 600;
        border-bottom: 2px solid #99C24D;
        padding-bottom: 0.3rem;
        margin-top: 1rem;
    }
    .highlight {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
        border-left: 4px solid #048BA8;
    }
    .contact-info {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
</style>
""", unsafe_allow_html=True)

# Updated Resume data with complete education history
resume_data = {
    "name": "Romit Deokar",
    "title": "First Year Student at SRM University",
    "stream": "Computer Science Engineering",
    "contact": {
        "phone": "8977007885",
        "email": "romitdeokar@gmail.com",
        "university_email": "rd3432@srmist.edu.in",
        "address": "7/73, Nagendra Nagar colony, Habsiguda, Hyderabad-500007"
    },
    "education": {
        "university": {
            "name": "SRM University, KTR",
            "degree": "B.Tech in Computer Science Engineering",
            "year": "2024-2028"
        },
        "intermediate": {
            "name": "Fiitjee Jr College",
            "year": "2022-2024",
            "details": "Inter second year (12th)"
        },
        "school": {
            "name": "Sarathi School",
            "details": "1st to 10th standard"
        }
    },
    "links": {
        "github": "https://github.com/RomitDeokar",
        "linkedin": "www.linkedin.com/in/romit-deokar-464b29332",
        "personal_website": ""  # Add your website when available
    },
    "skills": {
        "programming": ["C", "C++", "Java", "Python", "Problem Solving"],
        "database": ["SQL", "MySQL"],
        "web_dev": ["HTML", "CSS", "JavaScript"],
        "frameworks": [".NET in C#", "Streamlit", "Gradio"],
        "ml_dl": ["NumPy", "Pandas", "Matplotlib", "Neural Networks"],
        "learning": ["Lisp", "Mojo (in progress)"],
        "interests": ["Deep Learning", "ML", "NLP", "RAG"]
    },
    "future_goals": [
        "To gain professional skills",
        "Research on Deep Learning and quantum computing",
        "Get a good placement"
    ],
    "hobbies": [
        "Internet surfing and YouTube for new tech",
        "Listening to Music",
        "Social Media"
    ],
    "objective": "My objective is to gain professional and technical skills and knowledge by participating in many different and unique hackathons and internships from the first year itself. Although my coding experience is limited, I am eager to learn, actively participate, and enhance my understanding through hands-on experience."
}

# Updated Chatbot knowledge base with complete education information
knowledge_base = {
    "name": "My name is Romit Deokar.",
    "university": "I'm a first-year student at SRM University KTR, studying Computer Science Engineering.",
    "college": "I completed my intermediate education (11th-12th) at Fiitjee Jr College from 2022 to 2024.",
    "school": "I completed my schooling (1st to 10th standard) at Sarathi School.",
    "stream": "I'm studying Computer Science Engineering at SRM University.",
    "degree": "I'm pursuing a B.Tech in Computer Science Engineering (2024-2028).",
    "contact": "You can contact me at 8977007885 or via email at romitdeokar@gmail.com or rd3432@srmist.edu.in.",
    "location": "I'm from Hyderabad and my address is 7/73, Nagendra Nagar colony, Habsiguda, Hyderabad-500007.",
    "skills": "I know programming languages like C, C++, Java, Python, and have skills in SQL, HTML, CSS, JavaScript, .NET, Streamlit, and Gradio. I'm also familiar with ML libraries like NumPy, Pandas, and Matplotlib.",
    "interests": "I'm currently interested in Deep Learning, ML, NLP, and RAG.",
    "future_goals": "My future goals include gaining professional skills, researching Deep Learning and quantum computing, and getting a good placement.",
    "hobbies": "My hobbies include internet surfing and YouTube for new tech, listening to music, and social media.",
    "github": "You can find my GitHub at https://github.com/RomitDeokar",
    "linkedin": "My LinkedIn profile is www.linkedin.com/in/romit-deokar-464b29332",
    "objective": "My objective is to gain professional skills through hackathons and internships. I'm eager to learn and enhance my understanding through hands-on experience.",
    "education": "I'm currently studying B.Tech in Computer Science Engineering at SRM University KTR (2024-2028). I completed my intermediate education at Fiitjee Jr College (2022-2024) and my schooling (1st-10th) at Sarathi School.",
}

# Functions for the pages
def home_page():
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"<h1 class='main-header'>{resume_data['name']}</h1>", unsafe_allow_html=True)
        st.markdown(f"<p class='sub-header'>{resume_data['title']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='sub-header'>{resume_data['stream']}</p>", unsafe_allow_html=True)
        
        st.markdown("<p class='section-header'>About Me</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='highlight'>{resume_data['objective']}</div>", unsafe_allow_html=True)
        
    with col2:
        # Display contact information in a card-like format
        st.markdown("<p class='section-header'>Contact Information</p>", unsafe_allow_html=True)
        contact_info = f"""
        📱 Phone: {resume_data['contact']['phone']}  
        📧 Email: {resume_data['contact']['email']}  
        🏫 University: {resume_data['contact']['university_email']}  
        🏠 Address: {resume_data['contact']['address']}
        """
        st.markdown(contact_info)
        
        st.markdown("<p class='section-header'>Links</p>", unsafe_allow_html=True)
        st.markdown(f"🔗 [GitHub]({resume_data['links']['github']})")
        st.markdown(f"🔗 [LinkedIn]({resume_data['links']['linkedin']})")
        if resume_data['links']['personal_website']:
            st.markdown(f"🔗 [Personal Website]({resume_data['links']['personal_website']})")
    
    # Updated Education section with complete history
    st.markdown("<p class='section-header'>Education</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("University")
        st.write(f"**Institution:** {resume_data['education']['university']['name']}")
        st.write(f"**Degree:** {resume_data['education']['university']['degree']}")
        st.write(f"**Duration:** {resume_data['education']['university']['year']}")
    
    with col2:
        st.subheader("Intermediate")
        st.write(f"**Institution:** {resume_data['education']['intermediate']['name']}")
        st.write(f"**Duration:** {resume_data['education']['intermediate']['year']}")
        st.write(f"**Details:** {resume_data['education']['intermediate']['details']}")
    
    with col3:
        st.subheader("School")
        st.write(f"**Institution:** {resume_data['education']['school']['name']}")
        st.write(f"**Details:** {resume_data['education']['school']['details']}")
    
    # Skills section
    st.markdown("<p class='section-header'>Skills</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Programming")
        for skill in resume_data['skills']['programming']:
            st.write(f"• {skill}")
        
        st.subheader("Web Development")
        for skill in resume_data['skills']['web_dev']:
            st.write(f"• {skill}")
    
    with col2:
        st.subheader("Frameworks")
        for skill in resume_data['skills']['frameworks']:
            st.write(f"• {skill}")
        
        st.subheader("Database")
        for skill in resume_data['skills']['database']:
            st.write(f"• {skill}")
    
    with col3:
        st.subheader("ML/DL")
        for skill in resume_data['skills']['ml_dl']:
            st.write(f"• {skill}")
        
        st.subheader("Currently Learning")
        for skill in resume_data['skills']['learning']:
            st.write(f"• {skill}")
    
    # Current Interests
    st.markdown("<p class='section-header'>Current Interests</p>", unsafe_allow_html=True)
    interest_list = ", ".join(resume_data['skills']['interests'])
    st.write(interest_list)
    
    # Future Goals
    st.markdown("<p class='section-header'>Future Goals</p>", unsafe_allow_html=True)
    for i, goal in enumerate(resume_data['future_goals'], 1):
        st.write(f"{i}. {goal}")
    
    # Hobbies
    st.markdown("<p class='section-header'>Hobbies</p>", unsafe_allow_html=True)
    for i, hobby in enumerate(resume_data['hobbies'], 1):
        st.write(f"{i}. {hobby}")

def project_page():
    st.markdown("<h1 class='main-header'>Projects</h1>", unsafe_allow_html=True)
    st.write("This section can be expanded as you complete more projects.")
    
    # Example project (placeholder)
    st.markdown("<p class='section-header'>Streamlit Resume & Chatbot</p>", unsafe_allow_html=True)
    st.write("An interactive resume website with a built-in chatbot to answer questions about me.")
    st.write("**Technologies used:** Python, Streamlit, Natural Language Processing")
    
    # Add more projects as you complete them
    st.markdown("<p class='section-header'>Add Your Projects Here</p>", unsafe_allow_html=True)
    st.write("As you complete more projects, you can add them to this section with descriptions, links, and screenshots.")

def chatbot_page():
    st.markdown("<h1 class='main-header'>Chat with Romit-Bot</h1>", unsafe_allow_html=True)
    st.write("Ask me anything about Romit's experience, skills, or background!")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask something about Romit..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get response based on simple keyword matching
        response = get_chatbot_response(prompt)
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            # Initialize an empty string for the animated response
            animated_response = st.empty()
            
            # Simulate typing effect
            full_response = response
            displayed_response = ""
            for i in range(len(full_response) + 1):
                displayed_response = full_response[:i]
                animated_response.markdown(displayed_response)
                time.sleep(0.01)  # Adjust speed as needed
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

def get_chatbot_response(question):
    """Improved keyword-based response generation that can handle both Romit-specific
    questions and general conversation."""
    question = question.lower().strip()
    
    # Check for explicit questions about school and education first
    if any(phrase in question for phrase in ["school name", "name of school", "which school"]):
        return knowledge_base["school"]
    
    if any(phrase in question for phrase in ["college name", "junior college", "intermediate", "11th", "12th", "fiitjee"]):
        return knowledge_base["college"]
    
    # Check for specific questions about Romit
    if any(word in question for word in ["name", "who are you", "who is romit"]):
        return knowledge_base["name"]
    
    elif any(word in question for word in ["university", "college", "srm"]):
        return knowledge_base["university"]
    
    elif any(word in question for word in ["school", "where did you study", "high school", "sarathi"]):
        return knowledge_base["school"]
    
    elif any(word in question for word in ["stream", "branch", "major", "course", "cse", "computer science"]):
        return knowledge_base["stream"]
    
    elif any(word in question for word in ["contact", "phone", "email", "reach", "number"]):
        return knowledge_base["contact"]
    
    elif any(word in question for word in ["location", "address", "live", "from", "city", "hyderabad"]):
        return knowledge_base["location"]
    
    elif any(word in question for word in ["skill", "know", "programming", "language", "technologies", "code", "coding"]):
        return knowledge_base["skills"]
    
    elif any(word in question for word in ["interest", "focus", "working on", "passionate"]):
        return knowledge_base["interests"]
    
    elif any(word in question for word in ["goal", "plan", "future", "aspiration", "aim for"]):
        return knowledge_base["future_goals"]
    
    elif any(word in question for word in ["hobby", "free time", "leisure", "enjoy", "fun"]):
        return knowledge_base["hobbies"]
    
    elif any(word in question for word in ["github", "repository", "code repository", "projects"]):
        return knowledge_base["github"]
    
    elif any(word in question for word in ["linkedin", "professional", "profile", "professional network"]):
        return knowledge_base["linkedin"]
    
    elif any(word in question for word in ["objective", "aim", "target", "purpose", "mission"]):
        return knowledge_base["objective"]
    
    elif any(word in question for word in ["study", "studying", "education", "degree", "academic"]):
        return knowledge_base["education"]
    
    # General conversation responses for a more natural chatbot experience
    elif any(greeting in question for greeting in ["hello", "hi", "hey", "greetings"]):
        return "Hello! I'm Romit-Bot. How can I help you today?"
    
    elif any(phrase in question for phrase in ["how are you", "how's it going"]):
        return "I'm doing well, thanks for asking! How can I tell you about Romit today?"
    
    elif "thank" in question:
        return "You're welcome! Feel free to ask if you have any other questions about Romit."
    
    elif any(phrase in question for phrase in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"
        
    # Handle general questions about any topic
    elif any(word in question for word in ["weather", "temperature", "forecast"]):
        return "I don't have real-time weather information, but I'd be happy to tell you about Romit!"
    
    elif any(word in question for word in ["joke", "funny"]):
        return "Why don't programmers like nature? It has too many bugs! Is there anything about Romit you'd like to know?"
    
    elif any(word in question for word in ["time", "date", "day"]):
        return "I don't have real-time information, but I can tell you about Romit's education and skills instead!"
    
    # Default response with suggestions
    else:
        return "I don't have specific information about that. Feel free to ask about Romit's skills, education, contact information, or objectives! Some example questions: 'What school did Romit attend?', 'What are Romit's skills?', or 'What is Romit studying?'"

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Chat with Romit-Bot"])

# Display the selected page
if page == "Home":
    home_page()
elif page == "Projects":
    project_page()
else:
    chatbot_page()

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("© 2025 Romit Deokar")