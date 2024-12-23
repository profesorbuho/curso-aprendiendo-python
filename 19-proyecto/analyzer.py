from text_tools import (upload_file, analyze_text, search_replace, summary_generator)

print( "📘 Welcome to the Analyze text file's System 📘" )

file_path = input("👉 Enter the text file's path (.txt): ")
text = upload_file(file_path)

while True:
    print( "\n 💠 Options menu:" )
    print( "1️⃣  Analyze text" )
    print( "2️⃣  Search and replace using RegEx" )
    print( "3️⃣  Generate a text summary" )
    print( "4️⃣  Exit" )

    option = input( "Choose an option: " )

    if option == "1":
        try:
            results = analyze_text(text)
            print( "\n📊 Analyze results:" )
            for key, value in results.items():
                print( f"🔸{key}: {value}" )
        except Exception as e:
            print( f"❌ Error during analyzing text: {e}" )

    elif option == "2":
        regex = input( "👉 Enter the regex to find (regular expression): " )
        replace = input( "👉 Enter the replace text: " )
        modified_text = search_replace(text, regex, replace)
        print( "🔄️ All changes have been made succesfully." )
        print( "\n", modified_text )

    elif option == "3":
        try:
            summary = summary_generator(text)
            print( "\n📚 Generated summary:\n" )
            print( summary )
        except Exception as e:
            print( f"❌ Error during generating the summary: {e}" )

    elif option == "4":
        print( "👋 Thanks for using the Analyze text file's System!" )
        break

    else:
        print( "⚠️  No valid option. Try it again." )
