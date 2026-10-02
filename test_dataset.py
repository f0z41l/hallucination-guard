test_cases = [

    # France
    {
        "question": "What is the capital of France?",
        "answer": "The capital of France is Paris.",
        "expected": "Verified"
    },
    {
        "question": "What is the capital of France?",
        "answer": "The capital of France is London.",
        "expected": "Possible Hallucination"
    },

    # Eiffel Tower
    {
        "question": "Where is the Eiffel Tower located?",
        "answer": "The Eiffel Tower is located in Paris, France.",
        "expected": "Verified"
    },
    {
        "question": "Where is the Eiffel Tower located?",
        "answer": "The Eiffel Tower is located in Berlin, Germany.",
        "expected": "Possible Hallucination"
    },

    # Earth
    {
        "question": "Which planet is Earth from the Sun?",
        "answer": "Earth is the third planet from the Sun.",
        "expected": "Verified"
    },
    {
        "question": "Which planet is Earth from the Sun?",
        "answer": "Earth is the fifth planet from the Sun.",
        "expected": "Possible Hallucination"
    },

    # Python
    {
        "question": "Who created Python?",
        "answer": "Python was created by Guido van Rossum.",
        "expected": "Verified"
    },
    {
        "question": "Who created Python?",
        "answer": "Python was created by James Gosling.",
        "expected": "Possible Hallucination"
    },

    # Pacific Ocean
    {
        "question": "What is the largest ocean on Earth?",
        "answer": "The Pacific Ocean is the largest ocean on Earth.",
        "expected": "Verified"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "answer": "The Atlantic Ocean is the largest ocean on Earth.",
        "expected": "Possible Hallucination"
    },

    # Mount Everest
    {
        "question": "What is the highest mountain above sea level?",
        "answer": "Mount Everest is the highest mountain above sea level.",
        "expected": "Verified"
    },
    {
        "question": "What is the highest mountain above sea level?",
        "answer": "K2 is the highest mountain above sea level.",
        "expected": "Possible Hallucination"
    },

    # Sun
    {
        "question": "What is the Sun?",
        "answer": "The Sun is a star at the center of the Solar System.",
        "expected": "Verified"
    },
    {
        "question": "What is the Sun?",
        "answer": "The Sun is a planet at the center of the Solar System.",
        "expected": "Possible Hallucination"
    },

    # Water
    {
        "question": "What is the chemical formula of water?",
        "answer": "The chemical formula of water is H2O.",
        "expected": "Verified"
    },
    {
        "question": "What is the chemical formula of water?",
        "answer": "The chemical formula of water is CO2.",
        "expected": "Possible Hallucination"
    },

    # Human heart
    {
        "question": "What does the human heart do?",
        "answer": "The human heart pumps blood throughout the body.",
        "expected": "Verified"
    },
    {
        "question": "What does the human heart do?",
        "answer": "The human heart produces oxygen for the body.",
        "expected": "Possible Hallucination"
    },

    # Moon
    {
        "question": "What is the Moon?",
        "answer": "The Moon is Earth's natural satellite.",
        "expected": "Verified"
    },
    {
        "question": "What is the Moon?",
        "answer": "The Moon is a star orbiting Earth.",
        "expected": "Possible Hallucination"
    },

    # Amazon River
    {
        "question": "What is the Amazon River?",
        "answer": "The Amazon River is one of the world's largest rivers by water discharge.",
        "expected": "Verified"
    },
    {
        "question": "What is the Amazon River?",
        "answer": "The Amazon River is a desert in North Africa.",
        "expected": "Possible Hallucination"
    },

    # Sahara
    {
        "question": "Where is the Sahara Desert?",
        "answer": "The Sahara Desert is located in North Africa.",
        "expected": "Verified"
    },
    {
        "question": "Where is the Sahara Desert?",
        "answer": "The Sahara Desert is located in South America.",
        "expected": "Possible Hallucination"
    },

    # Java
    {
        "question": "What type of language is Java?",
        "answer": "Java is a high-level, object-oriented programming language.",
        "expected": "Verified"
    },
    {
        "question": "What type of language is Java?",
        "answer": "Java is a database management system.",
        "expected": "Possible Hallucination"
    },

    # CPU
    {
        "question": "What does a CPU do?",
        "answer": "A CPU executes instructions and performs calculations.",
        "expected": "Verified"
    },
    {
        "question": "What does a CPU do?",
        "answer": "A CPU is used only to store permanent files.",
        "expected": "Possible Hallucination"
    },

    # HTML
    {
        "question": "What is HTML used for?",
        "answer": "HTML is used to structure content on web pages.",
        "expected": "Verified"
    },
    {
        "question": "What is HTML used for?",
        "answer": "HTML is a programming language used only for database queries.",
        "expected": "Possible Hallucination"
    },
        # Neutral / insufficient evidence
    {
        "question": "Who created Python?",
        "answer": "Python is widely used in web development.",
        "expected": "Low Confidence"
    },
    {
        "question": "Where is the Eiffel Tower located?",
        "answer": "The Eiffel Tower attracts millions of tourists every year.",
        "expected": "Low Confidence"
    },
    {
        "question": "What is the Sun?",
        "answer": "The Sun provides light and heat to Earth.",
        "expected": "Low Confidence"
    },

    # Partially supported
    {
        "question": "Who created Python?",
        "answer": "Guido van Rossum created Python in 1991.",
        "expected": "Verified"
    },
    {
        "question": "What is the Moon?",
        "answer": "The Moon is Earth's natural satellite and is made of cheese.",
        "expected": "Possible Hallucination"
    },
    {
        "question": "What does a CPU do?",
        "answer": "A CPU executes instructions and stores permanent files.",
        "expected": "Possible Hallucination"
    },

    # Additional correct statements
    {
        "question": "Where is Mount Everest located?",
        "answer": "Mount Everest is located in the Himalayas.",
        "expected": "Verified"
    },
    {
        "question": "What is the chemical formula of water?",
        "answer": "Water contains hydrogen and oxygen and has the formula H2O.",
        "expected": "Verified"
    },
    {
        "question": "What is HTML?",
        "answer": "HTML is a markup language used to structure web pages.",
        "expected": "Verified"
    },

    # Additional contradictions
    {
        "question": "Where is Mount Everest located?",
        "answer": "Mount Everest is located in the Sahara Desert.",
        "expected": "Possible Hallucination"
    },
    {
        "question": "What is the chemical formula of water?",
        "answer": "Water has the chemical formula NaCl.",
        "expected": "Possible Hallucination"
    },
    {
        "question": "What is HTML?",
        "answer": "HTML is a database management system.",
        "expected": "Possible Hallucination"
    },

    # More neutral cases
    {
        "question": "What is the Amazon River?",
        "answer": "The Amazon River passes through every country in South America.",
        "expected": "Low Confidence"
    },
    {
        "question": "What is Java?",
        "answer": "Java was first released in 1995.",
        "expected": "Low Confidence"
    },
    {
        "question": "What does the human heart do?",
        "answer": "The human heart is about the size of a person's fist.",
        "expected": "Low Confidence"
    }
]

