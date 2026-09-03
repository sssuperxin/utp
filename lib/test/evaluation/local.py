from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/mnt/e/Datasets/got10k_lmdb'
    settings.got10k_path = '/mnt/e/Datasets/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.itb_path = '/mnt/e/Datasets/itb'
    settings.lasot_extension_subset_path_path = '/mnt/e/Datasets/lasot_extension_subset'
    settings.lasot_lmdb_path = '/mnt/e/Datasets/lasot_lmdb'
    settings.lasot_path = '/mnt/e/Datasets/lasot'
    settings.network_path = '/home/superxin/UTPTrack-O/output/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/mnt/e/Datasets/nfs'
    settings.otb_path = '/mnt/e/Datasets/otb'
    settings.prj_dir = '/home/superxin/UTPTrack-O'
    settings.result_plot_path = '/home/superxin/UTPTrack-O/output/test/result_plots'
    settings.results_path = '/home/superxin/UTPTrack-O/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/home/superxin/UTPTrack-O/output'
    settings.segmentation_path = '/home/superxin/UTPTrack-O/output/test/segmentation_results'
    settings.tc128_path = '/mnt/e/Datasets/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/mnt/e/Datasets/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/mnt/e/Datasets/trackingnet'
    settings.uav_path = '/mnt/e/Datasets/uav'
    settings.vot18_path = '/mnt/e/Datasets/vot2018'
    settings.vot22_path = '/mnt/e/Datasets/vot2022'
    settings.vot_path = '/mnt/e/Datasets/VOT2019'
    settings.youtubevos_dir = ''

    return settings

