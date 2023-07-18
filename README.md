# REMOTE-AUTOMATION-
Welcome to the Remote Automation project!. With this setup, anyone from anywhere can send commands via email to their PC, triggering various actions, such as opening files, initiating torrent downloads, and more. This project enables secure remote automation of tasks on a PC using email as the communication medium.

The system involves two email accounts: one for the user who initiates the commands and another for the PC that executes the specified tasks. Both email accounts are secure and under your control, ensuring that only authorized users can interact with the PC and perform automation tasks.

Security: The email accounts involved in this project are secure as they are exclusively in your possession. The PC's email account is configured securely using Google App Passwords, and Gmail is utilized for communication, minimizing hacking risks. Additionally, encryption can be employed for sensitive data, further enhancing security.


This is the video demonstration showcasing the process of sending an email via Gmail to open applications like Shareit and Matlab.

https://github.com/YASHASVASISHTA/REMOTE-AUTOMATION-/assets/112754882/ddd44fda-b8b5-4c54-b37d-963d3d3a054f

Confirmation Email: Upon successful execution of scheduled tasks, the PC will send a confirmation email back to the user's email account. This confirmation mechanism provides the user with feedback on task completion, ensuring transparency and keeping the user informed about the status of their automation commands.


Getting Started:

1. Clone the Repository
2. Replace Gmail and App Password:
   - Open the uploaded Python file in the project that contains the automation logic.
   - Look for all occurrences of `#GMAIL_ADDRESS` and replace them with your Gmail address from which you want to receive commands.
   - Replace all instances of `#16_DIGIT_APP_PASSWORD` with your 16-digit Google App Password. This is the password you generated for secure authentication.

3. Change Executable File Paths:
   - Examine the Python file to identify the locations where executables or files are being referenced.
   - Update these file paths to match the specific paths on your PC where the respective executables or files are located.

After completing these steps, you are ready to use the Remote Automation project. The modified Python file will be configured with your Gmail and App Password, and the executable file paths will point to the correct locations on your PC. Now you can safely run the project and start sending commands via email to automate tasks on your PC.
