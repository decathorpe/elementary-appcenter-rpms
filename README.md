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

| package name  | f28  | f29  | rawhide |
| ------------- | ---- | ---- | ------- |
| [aesop]       | DONE | DONE | DONE    |
| [alias]       | DONE | DONE | DONE    |
| [bookworm]    | DONE | DONE | DONE    |
| [hourglass]   | DONE | DONE | DONE    |
| [ideogram]    | DONE | DONE | DONE    |
| [nasc]        | DONE | DONE | DONE    |
| [nimbus]      | DONE | DONE | DONE    |
| [Notes-up]    | DONE | DONE | DONE    |
| [quilter]     | DONE | DONE | DONE    |
| [Spice-up]    | DONE | ---- | ----    |
| [taxi]        | DONE | DONE | DONE    |
| [tomato]      | DONE | DONE | DONE    |
| [tootle]      | DONE | DONE | DONE    |
| [Transporter] | ---- | DONE | DONE    |

[aesop]: https://github.com/lainsce/aesop
[alias]: https://github.com/bartzaalberg/alias
[bookworm]: https://github.com/babluboy/bookworm
[hourglass]: https://github.com/sgpthomas/hourglass
[ideogram]: https://github.com/cassidyjames/ideogram
[nasc]: https://github.com/parnold-x/nasc
[nimbus]: https://github.com/danrabbit/nimbus
[Notes-up]: https://github.com/Philip-Scott/Notes-up
[quilter]: https://github.com/lainsce/quilter
[Spice-up]: https://github.com/Philip-Scott/Spice-up
[taxi]: https://github.com/Alecaddd/taxi
[tomato]: https://github.com/luizaugustomm/tomato
[tootle]: https://github.com/bleakgrey/tootle
[Transporter]: https://github.com/bleakgrey/Transporter

