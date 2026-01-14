---
icon: material/download-outline
---

# How to install

Currently there is no prebuilt binaries, so the only way to obtain
dbuf is to build it from sources.

## Requirements

* `cargo` with version at least `1.91.1` which can be gained by official [rust website](https://rust-lang.org/).

## Build from sources

!!! info
    Currently building guaranteed to work only on Linux systems.

To build from sources run:

```bash
cargo install --git https://github.com/DependoBuf/dependobuf.git
```

That will install `dbuf` to system-wide. If you prefer to get binary use that instead:

```sh
cargo install --git https://github.com/DependoBuf/dependobuf.git --root $HERE
```

Where `$HERE` is directory where download metadata will be stored with binary at
`$HERE/build/bin/dbuf`.

## Language server

DependoBuf also has It's language server. To use it run `dbuf lsp`. Also there is
a [plugin](https://marketplace.visualstudio.com/items?itemName=DependoBuf.dependobuf)
in Visual Studio Code, that dramatically helps with editing .dbuf files.
!!! failure
    Currently shouldn't work due change to API of dbuf.
