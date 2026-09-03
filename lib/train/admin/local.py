class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/superxin/UTPTrack-O'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/superxin/UTPTrack-O/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/superxin/UTPTrack-O/pretrained_networks'
        self.lasot_dir = '/mnt/e/Datasets/LaSOT/LaSOT/zip'
        self.got10k_dir = '/mnt/e/Datasets/GOT-10k/train'
        self.got10k_val_dir = '/mnt/e/Datasets/GOT-10k/val'
        self.lasot_lmdb_dir = '/mnt/e/Datasets/lasot_lmdb'
        self.got10k_lmdb_dir = '/mnt/e/Datasets/got10k_lmdb'
        self.trackingnet_dir = '/mnt/e/Datasets/TrackingNet'
        self.trackingnet_lmdb_dir = '/mnt/e/Datasets/trackingnet_lmdb'
        self.coco_dir = '/mnt/e/Datasets/COCO2017'
        self.coco_lmdb_dir = '/mnt/e/Datasets/coco_lmdb'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/mnt/e/Datasets/vid'
        self.imagenet_lmdb_dir = '/mnt/e/Datasets/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = ''
        self.youtubevos_dir = ''
