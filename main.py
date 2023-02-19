from passgen import *
import flet as ft


def main(page: ft.page):  # main class to build the page
    page.title = "FirstPass"  # set page title
    page.bgcolor = "#243B53"  # set the background color
    page.theme_mode = "dark"  # set the page theming for dark elements
    # set up padding for the sides and top of the page
    page.padding = ft.padding.only(left=60, top=20, right=60)

    # page changes for elements when the Passphrase button is clicked
    def selectPassphrase(e):
        introText.visible = False
        optionView.visible = False
        textView.visible = True
        t.visible = True
        # sets the textField t value to what is returned from the passphrase function
        t.value = passphrase()
        generateBtn.visible = True
        copyBtn.visible = True
        backBtn.visible = True
        page.update()  # update page

    def selectPassword(e):  # page changes for elements when the Password button is clicked
        introText.visible = False
        userType = "all"  # sets userType value
        optionView.visible = False
        textView.visible = True
        t.visible = True
        # sets the textField t value to what is returned from the password function
        t.value = password(int(passLength.value), userType,
                           uppercaseBox.value, lowercaseBox.value, numbersBox.value, symbolsBox.value)
        copyBtn.visible = True
        generatePasswordBtn.visible = True
        backBtn.visible = True
        customView.visible = True
        page.update()  # updates page

    def copyVal(e):  # function to copy the textField t value to clipboard
        page.set_clipboard(t.value)
        page.update()  # updates page

    def generatePassphrase(e):  # function to generate a passphrase
        # sets textField t to the passphrase generated from passphrase function
        t.value = passphrase()
        page.update()

    def generatePassword(e):  # function to generate a password
        textView.visible = True
        if allCheckbox.value == True:  # sets userType to all characters if the checkbox is clicked
            userType = "all"
        if sayCheckbox.value == True:  # sets userType to easy to say if the checkbox is clicked
            userType = "say"
        if readCheckbox.value == True:  # sets userType to easy to read if the checkbox is clicked
            userType = "read"
        # updates the textField t value to what is generated in the password function
        t.value = password(passLength.value, userType,
                           uppercaseBox.value, lowercaseBox.value, numbersBox.value, symbolsBox.value)
        page.update()  # updates page

    def toInteger(e):  # converts the passLength textField value to an integer
        temp = passLength.value  # sets temp value to passLength value
        if temp.isdigit():  # checks if an integer value is inputted
            passLength.value = int(temp)  # sets passLength value to integer
            # sets the passLengthSlider value to the passLength value
            passLengthSlider.value = passLength.value
        page.update()  # updates page

    # function to update passLength textField value to the passLengthSlider value
    def slider_changed(e):
        passLength.value = int(e.control.value)
        page.update()  # updates page

    # function to update the value of the textField passLength and the slider to the length of the textField t
    def updateVal(e):  
        passLength.value = len(t.value)
        passLengthSlider.value = len(t.value)
        page.update()  # updates page

    # function to check if the easy to read checkbox is the only box selected 
    # or if none are selected
    def readableCheck(e):
        if readCheckbox.value == True:  # if checked, checks the other Ease of Use 
            # Types are selected and if the right subtypes are enabled
            sayCheckbox.value = False
            allCheckbox.value = False
            numbersBox.value = True
            symbolsBox.value = True
            numbersBox.disabled = False
            symbolsBox.disabled = False
        # checks if any checkbox has a value prompts user to select an Ease of Use Type (Easy to Read, 
        # Easy to Say, or All Characters)
        if readCheckbox.value == False and sayCheckbox.value == False and allCheckbox.value == False:  
            t.value = "Please select an Ease of Use Type"
        page.update()  # updates page
    # function to check if the easy to say checkbox is the only box selected or if none are selected
    def sayCheck(e): 
        # if checked, checks the other Ease of Use Types are selected and if the right subtypes are enabled
        if sayCheckbox.value == True: 
            allCheckbox.value = False
            readCheckbox.value = False
            numbersBox.value = False
            symbolsBox.value = False
            numbersBox.disabled = True
            symbolsBox.disabled = True
        # checks if any checkbox has a value prompts user to select an Ease of Use Type (Easy to Read, 
        # Easy to Say, or All Characters)
        if readCheckbox.value == False and sayCheckbox.value == False and allCheckbox.value == False:  
            t.value = "Please select an Ease of Use Type"
        page.update()  # updates page

    # function to check if the all characters checkbox is the only box selected or if none are selected
    def allCheck(e): 
        # if checked, checks the other Ease of Use Types are selected and if the right subtypes are enabled
        if allCheckbox.value == True:  
            readCheckbox.value = False
            sayCheckbox.value = False
            numbersBox.value = True
            symbolsBox.value = True
            numbersBox.disabled = False
            symbolsBox.disabled = False
        # checks if any checkbox has a value prompts user to select an Ease of Use Type 
        # (Easy to Read, Easy to Say, or All Characters)
        if readCheckbox.value == False and sayCheckbox.value == False and allCheckbox.value == False:  
            t.value = "Please select an Ease of Use Type"
        page.update()  # updates page

    # function checks if any subtype is selected
    def selectCheck(e): 
        if symbolsBox.value == False and numbersBox.value == False \
        and lowercaseBox.value == False and uppercaseBox.value == False:
            # prompts user to select a subtype (Symbols, numbers, lowercase, or uppercase)
            t.value = "Select a Subtype"
        page.update()  # updates page

    def backAction(e):  # function to go back to the initial elements on the page
        introText.visible = True
        optionView.visible = True
        textView.visible = False
        t.visible = False
        copyBtn.visible = False
        generatePasswordBtn.visible = False
        generateBtn.visible = False
        backBtn.visible = False
        customView.visible = False
        page.update()  # updates page

    def goToGithub(e):  # function to launch the github page for project
        page.launch_url("https://github.com/nanowtube/FirstPass")
        page.update()  # updates page

    def change_text(e):  # function to change the size of the textField t
        t.width = page.width * 0.8
        page.update()  # updates page
    # triggers the change_text function whenever the user resizes the page
    page.on_resize = change_text

    userType = ""  # sets the initial userType

    # inital text on screen when opening app
    introText = ft.Text(
        value="Generate Passphrase or \n Password?", size=25, text_align=ft.TextAlign.CENTER)

    # defines the textField where the password is displayed
    t = ft.TextField(width=page.width*0.8, border=ft.InputBorder.NONE, filled=True,
                     on_change=updateVal, multiline=True, text_size=18)

    # defines the button for the passphrase to be displayed and generated
    passphraseBtn = ft.ElevatedButton(
        "Passphrase", on_click=selectPassphrase, color="WHITE")
    # defines the button for the password to be displayed and generated
    passwordBtn = ft.ElevatedButton(
        "Password", on_click=selectPassword, color="WHITE")
    # defines the button to copy the text generated
    copyBtn = ft.ElevatedButton(
        "Copy", visible=False, on_click=copyVal, color="WHITE")
    # defines the button to generate the passphrase
    generateBtn = ft.ElevatedButton(
        "Generate", on_click=generatePassphrase, visible=False, color="WHITE")
    # defines the button to generate the password
    generatePasswordBtn = ft.ElevatedButton(
        "Generate", on_click=generatePassword, visible=False, color="WHITE")
    # defines the button to go back to the inital view
    backBtn = ft.ElevatedButton(
        "Go back", on_click=backAction, visible=False, color="WHITE")

    # defines the title text in the card view
    customText = ft.Text(value="Customize your password",
                         visible=True, size=20, weight="bold")

    # defines the textField for the password length
    passLength = ft.TextField(
        width=50, value=12, on_change=toInteger, border=ft.InputBorder.NONE,
        filled=True, focused_border_color="WHITE", text_align="center", border_radius=10)

    # defines the slider for the password length
    passLengthSlider = ft.Slider(min=0, max=50, divisions=50, value=int(passLength.value),
                                 on_change=slider_changed)

    # defines the Ease of Use checkboxes
    sayCheckbox = ft.Checkbox(label="Easy to Say", on_change=sayCheck)
    readCheckbox = ft.Checkbox(label="Easy to Read", on_change=readableCheck)
    allCheckbox = ft.Checkbox(
        value=True, label="All Characters", on_change=allCheck)

    # defines the subtype checkboxes
    uppercaseBox = ft.Checkbox(
        label="Uppercase", value=True, on_change=selectCheck)
    lowercaseBox = ft.Checkbox(
        label="Lowercase", value=True, on_change=selectCheck)
    numbersBox = ft.Checkbox(
        label="Numbers", value=True, on_change=selectCheck)
    symbolsBox = ft.Checkbox(
        label="Symbols", value=True, on_change=selectCheck)

    # defines row to show the FirstPass logo
    logoView = ft.Row([ft.Image(
        src=f"/icons/firstpass.png",
        width=100,
        height=100
    )], alignment=ft.MainAxisAlignment.CENTER)

    # defines row to display the introText
    introView = ft.Row([introText], alignment=ft.MainAxisAlignment.CENTER)

    # defines row to display the options for passphrase and password
    optionView = ft.Row([passphraseBtn, passwordBtn], spacing=20,
                        alignment=ft.MainAxisAlignment.CENTER)

    textView = ft.Column(  # puts all the textField and buttons related to the textField
        [
            ft.Row(
                [
                    t
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(
                [
                    copyBtn, generateBtn, generatePasswordBtn, backBtn
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        spacing=10,
        visible=False
    )

    customView = ft.Card(  # defines all the element placements within a card view
        content=ft.Column(
            [
                ft.Text(value="", size=5),
                ft.Row(
                    [
                        customText
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Divider(),  # adds divider to the card
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Column(
                                                [
                                                    ft.Text(
                                                        value="Password length"),
                                                    ft.Row(
                                                        [
                                                            passLength,
                                                            passLengthSlider,
                                                        ]
                                                    )
                                                ]
                                            ),
                                        ], alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        [
                                            ft.Column(
                                                [
                                                    sayCheckbox,
                                                    readCheckbox,
                                                    allCheckbox
                                                ]
                                            ),
                                            ft.Column(
                                                [
                                                    uppercaseBox,
                                                    lowercaseBox,
                                                    numbersBox,
                                                    symbolsBox
                                                ]
                                            )
                                        ], alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                spacing=10,
                            )
                        )
                    ],
                    spacing=10,
                ),
                ft.Text(value="", size=5),
            ],
            spacing=10
        ), visible=False, elevation=3.0
    )

    githubIconView = ft.Row(  # defines the row where the Github logo and link is displayed
        [
            ft.IconButton(
                content=ft.Image(src=f"/icons/github.png",
                                 width=30, height=30),
                icon_color="blue400",
                on_click=goToGithub,
                icon_size=20,
                tooltip="View in Github",
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER)

    page.add(  # adds all the elements to the page for utilization
        logoView,
        introView,
        optionView,
        textView,
        customView,
        githubIconView
    )


# sets target, sets application to open in the web browser, defines the assets directory
ft.app(target=main, view=ft.WEB_BROWSER, assets_dir="assets")
