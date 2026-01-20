# Creating a Dictionary
import streamlit as st
# Different Languages
ebira_dictionary = { #James Victor Bashayi BHU/25/04/09/0160
    'father' : 'Àdá',
    'house':'irehi',
    'light': 'Ira ',
    'hello': 'Ngwao',
    'sleep' : 'ara',
    'earth' : 'èhè',
    'song' : 'àhè',
    'truth' : 'Izeyiza',
    'broom' : 'oohi',
    'food' : 'ebae',
    'you' : 'ewu',
    'spoon' : 'ishivi',
    'meat' : 'uye',
    'goodbye': 'adijo',
    'thank you': 'avo',
    'yes' : 'ee',
    'come' : 'bẹ',
    'go' : 'na',
    'look' : 're',
    'money': 'ekehi'
}

igbo_dictionary = { #Anyanwu Ebenezer Ugonnaya BHU/25/04/09/0123
    'come':'bia',
    'hand':'aka',
    'meat':'anu',
    'ear':'nti',
    'fufu':'akpu',
    'here':'nga',
    'spoon':'ngaji',
    'cloth':'efe',
    'plate':'efere',
    'stomach':'afo',
    'head':'ishi',
    'house':'ulo',
    'cup':'iko',
    'pot':'ite',
    'yam':'gji',
    'poo':'nshi',
    'food':'nri',
    'water':'nmiri',
    'one':'otu',
    'two':'eibo'
}

edo_dictionary = { #Chidi Nwana Nelson BHU/25/04/10/0043
    "hello": "koyo",
    "water": "ami",
    "food": "ikhian",
    "house": "owa",
    "come": "ya",
    "go": "gha",
    "man": "okpia",
    "woman": "okhuo",
    "child": "omo",
    "good": "noghie",
    "bad": "khi",
    "sun": "owia",
    "moon": "okhuo-owia",
    "fire": "urhie",
    "name": "erhan",
    "money": "owo",
    "school": "ikpoba",
    "book": "ebo",
    "run": "khiagbe",
    "eat": "ya"
}

hausa_dictionary = {
    "hello": "Sannu",
    "come": "Zo",
    "go": "Tafi",
    "father": "Uba",
    "mother": "Uwa",
    "boy": "Yaro",
    "bye": "Sai anjima",
    "good morning": "Ina kwana",
    "good evening": "Barka da yamma",
    "welcome": "Maraba",
    "thank you": "Nagode",
    "food": "Abinci",
    "how are you": "Yaya kake?",
    "girl": "Yarinya",
    "money": "Kudi",
    "what is your name": "Menene sunanka?",
    "brother": "Dan'uwa",
    "sister": "Yar'uwa",
    "school": "Makaranta",
}

yoruba_dictionary = {
    "mother" : "iya",
    "shoes" : "bata",
    "water" : "omi",
    "no" : "rara",
    "father": "baba",
    "good morning": "ekaro",
    "where": "nibo",
    "stand": "duro",
    "walk": "rin",
    "drink": "mu",
    "place": "ibi",
    "come": "wa",
    "go": "lo",
    "a question marker(like 'is it')": "se",
    "sorry": "pele",
    "car": "olo",
    "hello": "e nle o!",
    "house": "ile",
    "child" : "omo",
    "cat" : "ologbo",
}
languages = {
    "Ebira" : ebira_dictionary,
    "Igbo" : igbo_dictionary,
    "Edo" : edo_dictionary,
    "Hausa" : hausa_dictionary,
    "Yoruba" : yoruba_dictionary,
}

    # <------------WITHOUT STREAMLIT--------->
# print("English to Local Language Translator")
# print("Available languages:")
#
# for lang in languages:
#     print(f"- {lang.capitalize()}")
#
# language = input("\nSelect a language: ").strip().lower()
#
# if language == "ebira":
#     dictionary = ebira_dictionary
# elif language == "igbo":
#     dictionary = igbo_dictionary
# elif language == "edo":
#     dictionary = edo_dictionary
# elif language == "hausa":
#     dictionary = hausa_dictionary
# elif language == "yoruba":
#     dictionary = yoruba_dictionary
# else:
#     print("Error: Language not supported.")
#     exit()
#
# word = input("Enter an English word to translate: ").strip().lower()
# translation = dictionary.get(word)
#
# if translation:
#     print(f"Translation: {translation}")
# else:
#     print("Error: Word not found in the selected dictionary.")

    # <---------------WITH STREAMLIT--------------->
st.title("LANGUAGE TRANSLATOR")
st.markdown("This App translates English to African/Local Languages")

st.divider()
# Create selection box for language
language = st.selectbox("Select a language:",languages)

if language:
    selected_dictionary = languages[language]
    word = st.selectbox("Select a word:",selected_dictionary)

st.divider()

if word:
    translation = selected_dictionary.get(word)
    if translation:
        st.success(f"Translation: {word} in {language} is '{translation}'")
    else:
        st.error(f"Translation: {word} in {language} is not available")

st.divider()
# st.balloons()
st.write("Thank you for using the app")
st.feedback()