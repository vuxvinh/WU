<html>
    <head>
        <title>Home</title>
    </head>

    <body>
        <a href="#">Home</a><?php echo "\t"?><a href="upload.html">Upload</a>
        <h1>List images</h1>
        <ul>
            <?php
                $files = array_diff(scandir("upload/images/"), array('..', '.'));           // array tao ra 1 mang gom 2 phan tu: . va .. // array_diff tra ve phan tu khac trong 2 mang so sanh
                foreach ($files as $file) {                                                 // in ra cac file upload
                    echo "<li><a href='upload/images/$file'>$file</li>";
                }?>
        </ul>
    </body>
</html>