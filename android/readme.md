# Android

## Create file in shared storage (external)

You can create shared files from your application by placing them in the shared storage directory.
To obtain the root path for the directory use `Environment.getExternalStorageDirectory()` method. 
This directory can hold data that is shared across all applications and can be mounted by the user on their computer.
Consider placing your files under subdirectory to avoid polluting the root directory.

In order to make your files visible for the user you need to call the `MediaScannerConnection.scanFile` method.

Following code snippet creates a new subdirectory with a name stored in the `dirName` variable
and creates a text file with a name of current date. The contents of the file is stored in the `fileContents` variable.

```java
String dirName = "MyData";
String fileContents = "Hello, World!";

String dirPath = Environment.getExternalStorageDirectory() + "/" + dirName;
File dir = new File(dirPath);
if (!dir.exists()) {
  dir.mkdirs();
}

SimpleDateFormat formatter = new SimpleDateFormat("yyyy_MM_dd_HH_mm_ss", Locale.US);
Date now = new Date();
String fileName = formatter.format(now) + ".txt";
File file = new File(dir, fileName);
if (file.exists()) {
  file.delete();
}

try {
  FileOutputStream fs = new FileOutputStream(file);
  fs.write(fileContents.getBytes(StandardCharsets.UTF_8));
  fs.close();

  MediaScannerConnection.scanFile(getApplicationContext(), new String[]{file.getAbsolutePath()}, null,null);
} catch(FileNotFoundException ex) {
  //TODO: handle FileNotFoundException
} catch(IOException ex) {
  //TODO: handle IOException
}
```
