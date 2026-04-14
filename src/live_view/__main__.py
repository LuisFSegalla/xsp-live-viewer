"""main."""

from optparse import OptionParser

from live_view.zmq_client_xspress import live_viewer


def main():
    """Main entrypoint."""
    parser = OptionParser()
    parser.add_option("-t",
                      "--stype",
                      action="store",
                      type="string",
                      dest="stype",
                      default="PULL")
    parser.add_option("-p",
                      "--host",
                      action="store",
                      type="string",
                      dest="host",
                      default="tcp://0.0.0.0:15510")
    (inputs, _) = parser.parse_args()
    print(f"Args: {inputs.stype} {inputs.host}")
    live_viewer(inputs.stype, inputs.host)


if __name__ == "__main__":
    main()
