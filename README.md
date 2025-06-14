# Custom-Terminal-Commands
## **Introduction :**
This project uses a ```.bat``` script to run custom terminal commands on **Windows**. The batch file is designed to execute a specific Python script or other executable files with ease.

## **Installation :**

```
# Clone the files 
git clone https://github.com/hydro-7/Custom-Terminal-Commands.git
```

The path will now be something like : ```../../Custom-Terminal-Commands```

Add this path to the User Environment Variables :
1. Win + S
2. Type "Edit the system environment variables" and enter
3. Click on "Environment Variables.."
4. Under "User variables for [your_username]", scroll to the path variable and click edit.
5. Click on "New" and add the Custom-Terminal_Commands path here

## **Commands :**

#### 1. ascii :
Converts the image file you have into ascii art and prints it onto the screen. It has params such as ```--file``` for the file name, ```--scale``` for the scale of the image generated, ```--cols``` which controls the width and ```--morelevels``` for more icons in the ascii generation.\
\
Hence, the command to use it would be as follows : ```ascii --file <filepath>``` where the other params are optional.
