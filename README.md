# Empty Folder Cleaner

## Table Of Contents

- [Description](#description)
- [Libaries Used](#libaries-used)
- [Setup Instructions](#setup-instructions)
- [How it works](#how-it-works)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Meet our contributors](#meet-our-contibutors)
- [License](#license)

## Description

Empty Folder Cleaner is a program that deletes empty folders from your computer or device and removes clutter to improve performance. It supports only windows and android for now.

## Libaries Used

- [Time](https://docs.python.org/3/library/time.html)
- [OS](https://docs.python.org/3/library/os.html)
- [Platform](https://docs.python.org/3/library/platform.html)

## Setup instructions

There are no prerequisites; simply run the script. If you don't already have Python installed, you can get it [here](https://www.python.org/downloads/).

- Clone the repository
```
git clone https://github.com/dark-coder-cat/Empty-Folder-Cleaner.git
```
- Go to the folder directory
```
cd empty-folder-cleaner
```
- Run the script
```
python empty_folder_cleaner.py
```

## How it works   

The program removes any empty folder(s) fom your device by:
- Checking the empty folders in curent path.
- Checking the empty folder in given path provided by user.

> Note: If you get any code like `03m[` on your terminal choose OPTION 3 before providing the path to be checked. 
> Option 3 is used to change the text color but it doesn't work on some devices or computer.

After providing the path to be checked, you'll be required to enter (Y/N) to confim the deletion of the folders.
Upon deletion, the follwoing would be displayed: 
  - The number of folders deleted.
  - The numebr of folders scanned.
  - The number of files and folders present in the provided path.
  - The scanned dir path.

> Enter **exit** at any input to stop the program.


## Screenshots

<table >
  <tr>
    <td colspan=2 align=center>Starting Screen<img src= "Images/startScreen.jpg" alt="startScreen.jpg">↙↘ </td>
  </tr>
  <tr>
    <td rowspan=2>Option 1<img src= "Images/Option1.jpg" alt="Option1.jpg"></td>
    <td>Option 2<img src= "Images/Option2.jpg" alt="Option2.jpg"></td>
  </tr>
  <tr>
    <td>Process<img src= "Images/Option2process.jpg" alt="Option2process.jpg"></td>
  </tr>
  <tr>
    <td colspan=2 align=center>↙if↘</td>
  </tr>
  <tr>
    <td>Found Empty Folders<img src= "Images/foundEmpty.jpg" alt="foundEmpty.jpg"></td>
    <td>Not Found Empty Folders<img src= "Images/noEmpty.jpg" alt="noEmpty.jpg"></td>
  </tr>
  <tr>
    <td colspan=2 align=center>↘↙</td>
  </tr>
  <tr>
    <td colspan=2 align=center>End Screen<img src="Images/endScreen.jpg" alt="endScreen.jpg"></td>
  </tr>
</table>

## Contributing

Feel free to add more features to this repo by either creating an issue or making a Pull Request. See our [contribution guidelines](CONTRIBUTING.md) to get started.

## Meet our contributors

<a href="https://github.com/dark-coder-cat/Empty-Folder-Cleaner/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dark-coder-cat/Empty-Folder-Cleaner" />
</a>

## License

This project is under an [MIT LICENSE](LICENSE)
