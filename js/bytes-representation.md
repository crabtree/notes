# Bytes representation

## Convert JS number to bytes

Convert to Big Endian bytes representation

```js
const num = 10; // 0x0A
const buf = Buffer.alloc(8);
buf.writeDobuleBE(num); // 0x40 0x24 0x00 0x00 0x00 0x00 0x00 0x00
buf.readDoubleBE(); // 10
```

Convert to Little Endian bytes representation

```js
const num = 10; // 0x0A
const buf = Buffer.alloc(8);
buf.writeDobuleLE(num); // 0x00 0x00 0x00 0x00 0x00 0x00 0x24 0x40
buf.readDoubleLE(); // 10
```