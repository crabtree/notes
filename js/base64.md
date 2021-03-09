# Base64

## Encode string to Base64

```js
const data = "foobar";
const encoded = Buffer
  .from(data)
  .toString("base64");
```

## Decode from Base64 to string

```js
const encoded = "Zm9vYmFy";
const decoded = Buffer
  .from(encoded, "base64")
  .toString("utf8");
```

## Encode binary data to Base64

```js
const fs = require("fs");
const data = fs.readFileSync("file.bin");
const encoded = data.toString("base64");
```

## Decode binary data from Base64

```js
const fs = require("fs");
const data = "..."; // some Base64 encoded binary data
const binary = Buffer.from(data, "base64");
fs.writeFileSync("file.bin", binary);
```