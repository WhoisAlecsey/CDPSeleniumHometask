class Constants:
    search_box = '//*[@id="searchbox"]/input'
    see_all_results = '//*[@class="button button-white devsite-suggest-all-results"]'
    google_cloud_calculator_link = '//*[@data-ctorig="https://cloud.google.com/products/calculator/"]'
    compute_engine_tab = '//*[@title="Compute Engine"]'
    number_of_instances = '//*[@name="quantity"]'
    operating_system = '//*[@ng-model="listingCtrl.computeServer.os"]'
    operating_system_value_free = '//*[@value="free"]'
    machine_class = '//*[@aria-label="VM Class: Regular"]'
    # machine_class_value_regular = '//*[@value="regular"]'
    machine_class_value_regular = '//*[@id="select_option_68"]/div[1]'
    machine_type = '//*[@placeholder="Instance type"]'
    # machine_type_value_n1_standard_8 = '//*[@value="CP-COMPUTEENGINE-VMIMAGE-N1-STANDARD-8"]'
    machine_type_value_n1_standard_8 = '//*[@id="select_option_210"]/div[1]'
    add_gpus = '//*[@aria-label="Add GPUs"]'
    number_of_gpus = '//*[@placeholder="Number of GPUs"]'
    # number_of_gpus_value_1 = '//*[@value="1"]'
    number_of_gpus_value_1 = '//*[@id="select_option_355"]'
    gpu_type = '//*[@placeholder="GPU type"]'
    gpu_type_value_tesla_v100 = '//*[@value="NVIDIA_TESLA_V100"]'
    local_ssd = '//*[@placeholder="Local SSD"]'
    local_ssd_value_2x375 = '//*[@id="select_option_231"]'
    datacenter_location = '//*[@placeholder="Datacenter location"]'
    datacenter_location_value_frankfurt = '//*[@id="select_option_180"]'
    commited_usage = '//*[@placeholder="Committed usage"]'
    commited_usage_value_1_year = '//*[@id="select_option_84"]'
    add_to_estimate = '//*[@aria-label="Add to Estimate"]'

    #Estimate Tab
    estimate_vm_class = '//*[@id="compute"]/md-list/md-list-item[2]/div'
    estimate_instance_type = '//*[@id="compute"]/md-list/md-list-item[3]/div'
    estimate_region = '//*[@id="compute"]/md-list/md-list-item[4]/div'
    estimate_available_ssd = '//*[@id="compute"]/md-list/md-list-item[5]/div'
    estimate_commitment_term = '//*[@id="compute"]/md-list/md-list-item[6]/div'
