---
icon: "lucide/rocket"
---

# Introduction

* [ ] intro page
* [ ] user downlaod page
* [ ] user docs
* [ ] lexers
* [ ] type checks

```dbuf
message Example {
  x Int;
  y String;
}
```

```dbuf
enum Example2 (x Int) {
  1 => {
    Ctr1
  }
  * => {
    Ctr2
  }
}
```
