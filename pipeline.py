import omni.usd
from pxr import Usd

def run(nucleus_server_base, simulation_app, send_progress):
    print("Pipeline started", flush=True)

    tree_path = f"{nucleus_server_base}/NVIDIA/Assets/Vegetation/Trees/American_Beech.usd"

    res, local_path = omni.client.get_local_file(tree_path)
    print("Get local result:", res)

    send_progress(10)

    if res == omni.client.Result.OK:
        stage = Usd.Stage.Open(local_path)
        send_progress(20)

        if stage:
            print("Stage opened", flush=True)
        else:
            print("Failed to load stage", flush=True)
    else:
        print("Failed to get local file:", res)

    simulation_app.update()
    send_progress(90)
    print("Pipeline finished", flush=True)