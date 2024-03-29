import subprocess

def install_dependencies():
    required_packages = ["bleak", "python-osc"]

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call(["pip", "install", package])

if __name__ == "__main__":
    install_dependencies()
    import asyncio
    from bleak import BleakScanner, BleakClient
    from pythonosc import udp_client

    HEART_RATE_UUID = "00002a37-0000-1000-8000-00805f9b34fb"

    POLAR_H10_NAME = "Polar H10 B71CC122"

    # Replace the following values with your VRChat IP and port
    vrchat_ip = "127.0.0.1"
    vrchat_port = 9000

    osc_client = udp_client.SimpleUDPClient(vrchat_ip, vrchat_port)

    async def run():
        retry_interval = 10  # seconds
        while True:
            try:
                devices = await BleakScanner.discover()

                polar_h10_device = None
                for device in devices:
                    if device.name and POLAR_H10_NAME in device.name:
                        polar_h10_device = device
                        break

                if polar_h10_device:
                    print(f"Found Polar H10: {polar_h10_device}")
                    async with BleakClient(polar_h10_device.address) as client:
                        await client.start_notify(HEART_RATE_UUID, handle_heart_rate)

                        try:
                            while True:
                                await asyncio.sleep(1)

                        except KeyboardInterrupt:
                            print("Exiting gracefully.")
                            await client.stop_notify(HEART_RATE_UUID)
                            break

                else:
                    print("Polar H10 not found. Retrying in {} seconds.".format(retry_interval))
                    await asyncio.sleep(retry_interval)

            except Exception as e:
                print(f"Error: {e}")
                print("Retrying in {} seconds.".format(retry_interval))
                await asyncio.sleep(retry_interval)

    def handle_heart_rate(sender: int, data: bytearray):
        heart_rate = data[1]
        print(f"Heart Rate: {heart_rate}")

        ones_hr = heart_rate % 10
        tens_hr = (heart_rate // 10) % 10
        hundreds_hr = (heart_rate // 100) % 10

        osc_client.send_message("/avatar/parameters/hr/ones_hr", ones_hr)
        osc_client.send_message("/avatar/parameters/hr/tens_hr", tens_hr)
        osc_client.send_message("/avatar/parameters/hr/hundreds_hr", hundreds_hr)
        osc_client.send_message("/avatar/parameters/hr/heart_rate", heart_rate)

    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        pass
