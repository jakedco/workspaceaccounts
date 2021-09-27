            +-----------------------------------------------------------+
            | deprecated; amazon made switching registrations a feature |
            +-----------------------------------------------------------+

                                +------------------+
                                | requires python3 |
                                +------------------+
                                 | made for macOS |
                                 +----------------+
              
              +---------------------------------------------------------+
              |    Reason: If someone has multiple Amazon Workspaces    |
              |          for different organizations, different         |
              |             registration codes are required.            |
              | (and I personally think the built in way takes too long |
              |           to switch between registration codes)         |
              +---------------------------------------------------------+

   +------------------------------------------------------------------------------+
   | Setup: After setting up one workspace, navigate to this directory in Finder: |
   |  ~/Library/Application Support/Amazon Web Services/Amazon WorkSpaces/        |
   |    From there, you want to take the "RegistrationList.json" and              |
   |    "UserSettings.json" files and place them in a folder. (And ideally name   |
   |    the folder the organization name.) Place workspaceaccounts.py in the      |
   |    same folder as your organization folders. Then you can run it using       |
   +----------------------+ "python3 workspaceaccounts.py" +----------------------+
                          +--------------------------------+
