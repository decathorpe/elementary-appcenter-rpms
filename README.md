# elementary-appcenter-rpms

I use this repository to keep track of files related to packaging / building
stable releases of "made for elementary" applications for fedora - either as a
staging ground before they can be imported as official fedora packages, or as
an external repository for applications that won't be accepted as proper fedora
packages (for various reasons) - yet.


## Known Issues

- The `hourglass` daemon might crash when first starting the application when
  no timers have been created.


## Package Status

The current build status of all non-official fedora packages can be seen at
<https://copr.fedorainfracloud.org/coprs/decathorpe/elementary-appcenter/monitor/>.

| package name | f27  | f28  | f29  | rawhide |
| ------------ | ---- | ---- | ---- | ------- |
| [bookworm]   | DONE | DONE | DONE | DONE    |
| [hourglass]  | DONE | DONE | DONE | DONE    |
| [nasc]       | DONE | DONE | DONE | DONE    |
| [nimbus]     | DONE | ---- | ---- | ----    |
| [quilter]    | DONE | DONE | DONE | DONE    |
| [Spice-up]   | ---- | DONE | DONE | DONE    |
| [tomato]     | DONE | DONE | DONE | DONE    |

[bookworm]: https://github.com/babluboy/bookworm
[hourglass]: https://github.com/sgpthomas/hourglass
[nasc]: https://github.com/parnold-x/nasc
[nimbus]: https://github.com/danrabbit/nimbus
[quilter]: https://github.com/lainsce/quilter
[Spice-up]: https://github.com/Philip-Scott/Spice-up
[tomato]: https://github.com/luizaugustomm/tomato

