# Ten years of the Venezuelan crisis

This repository contains the code, data, and figure the paper entitled _Ten years of the Venezuelan crisis - An Internet perspective_ that appear at [ACM SIGCOMM 2024](https://conferences.sigcomm.org/sigcomm/2024/). This paper is authored by Esteban Carisimo, Rashna Kumar, Caleb J. Wang and Fabián E. Bustamante. The paper is available [here](https://estcarisimo.github.io/assets/pdf/papers/2024-sigcomm-venezuela.pdf).



## Repository structure

### Data (`./data/`)

The `./data/` directory can be downloaded from this [link to Google Drive](https://drive.google.com/drive/folders/17U65vO1cG6QT-MWw0eovgRVR-J1DUK-P).

<b style="color: red;">Please note: Some datasets in this repository need to be retrieved using scripts. Carefully read the instructions provided in the sections below.</b>

Description of files/directories:

#### Raw data

- `./data/raw/02-pfx2as`: This directory contains [CAIDA's prefix-to-as mapping](https://www.caida.org/catalog/datasets/routeviews-prefix2as/) files. To populate this directory, please execute the script `./scripts/download-pfx2as.py`.
- `./data/raw/03-15-peeringdb`: This folder contains [CAIDA's monthly snapshots of PeeringDB data](https://www.caida.org/catalog/datasets/peeringdb/). To populate this directory, please run the script `./scripts/download-peeringdb.py`.
- `./data/raw/10-peeringdb`: This is a mirror directory of `./data/raw/03-15-peeringdb`, containing identical data.
- `./data/raw/05-facebook-ipv6`: This directory Meta's report on IPv6 adoption across each country in the LACNIC region.
- `./data/processed/08-asrel`: This folder provides [CAIDA's AS relatioships](https://www.caida.org/catalog/datasets/as-relationships/) files. Run `./scripts/download_asrel.py` to populate this directory.
- `./data/processed/08-delegated-lacnic`: This directory contains [LACNIC delegation files](https://ftp.lacnic.net/pub/stats/lacnic/). To populate this directory, run `./scripts/download-lacnic-delfiles.py`.
- `./data/raw/10-apnic-eyeballs`: Snapshot from [APNIC's Eyebeall Population Estimates](https://stats.labs.apnic.net/aspop) as of March 22, 2022.
- `./data/raw/11-mlab`: This directory holds monthly median download speeds measured by MLAB's NDT tests for all countries in the LACNIC region.
- `./data/raw/12-20-google-dns`: This directory offers files for per-probe monthly RTT measurements to Google Public DNS resolvers from RIPE Atlas probes in the LACNIC region since 2014 (measurement ID: 1591146).

#### Processed data

- `./data/processed/02-addr-space/02-addr_space_ve.csv.gz`: This file includes data on the address space allocated to Venezuela, detailing the space announced by each provider.
- `./data/processed/06-16-chaos-txt`: Contains files with locations of Root DNS servers inferred from DNS CHAOS TXT measurements. These measurements were conducted using RIPE Atlas probes in Venezuela since 2016.
- `./data/processed/07-hgs`: This directory holds data on _off-nets_ inferred to be in Venezuela obtained from the artifacts offered by Gigis et al. ( SIGCOMM 2021).
- `./data/processed/12-google-dns`: Stores the mean and median Round-Trip Time (RTT) latency values to Google Public DNS resolvers from RIPE Atlas probes in the LACNIC region since 2014 (measurement ID: 1591146).
- `./data/processed/12-stable-set`: Similar to the previous dataset but includes only measurements from probes that participated in at least 90% of the measurements, providing a stable set of RTT latency data.
- `./data/processed/17-ripe-probes`: Contains monthly data on the count of RIPE Atlas probes in each country within the LACNIC region.
- `./data/processed/19-third-party-providers`: Offers an analysis of the adoption of third-party providers in topsites across Latin American countries.

#### External data

- `./data/processed/01-a-crude_oil_production.csv`: Contains crude oil production data as reported by the OECD.
- `./data/processed/rir.csv`: Provides a list of Regional Internet Registries (RIRs).

If any of the external links or information on this page are broken or out of date, please feel free to create an issue on this repository.

###  Notebooks (`./notebooks`)

The `./notebooks` directory contains the Jupyter notebooks files used for all the analyses in the paper


- `./notebooks/01-econ-background.ipynb`: Presents the socioeconomic context in Venezuela as described in Section 2.
- `./notebooks/02-14-addr-space.ipynb`: Analyzes the role of CANTV in Venezuela's address space, detailed in Section 4.
- `./notebooks/03-peering-facilities.ipynb`: Describes the growth of peering facilities in Venezuela and the rest of Latin America using PeeringDB information, as shown in Section 5.1.
- `./notebooks/04-submarine-cable-network.ipynb`: <b style="color: red;">(Telegeography Submarine Cable map access restricted)</b> Compares the growth of submarine cable network (SCN) infrastructure in Venezuela with other LACNIC countries, as illustrated in Section 5.2.
- `./notebooks/05-facebook-ipv6-adoption-checkpoint.ipynb`: Examines the growth of IPv6 adoption in the LACNIC region, highlighting Venezuela's lag, as shown in Section 5.3.
- `./notebooks/06-chaos-txt.ipynb`: Utilizes RIPE Atlas DNS CHAOS TXT measurements to identify local mirrors of Root DNS servers deployed in Venezuela as analyzed in Section 5.4.
- `./notebooks/07-18-cdn-deployments.ipynb`: Leverages artifacts from Gigis et al. (SIGCOMM 2021) to assess the deployment of _off-nets_ across LACNIC operators which is presented in Section 5.5.
- `./notebooks/08-09-cantv-asrel.ipynb`: Uses CAIDA's AS relationship files to track changes in CANTV's upstream connectivity displayed in Section 6.1.
- `./notebooks/10-21-ixps.ipynb`: Uses PeeringDB data to compare Venezuela's presence at Internet Exchange Points (IXPs) with that of other Latin American countries, explained in Section 6.2.
- `./notebooks/11-bandwidth-mlab.ipynb`: Analyzes the evolution of download speeds in Venezuela and the LACNIC region using MLAB data, which is discussed in Section 7.1.
- `./notebooks/12-google-dns.ipynb`: Examines latency to Google Public DNS resolvers.
- `./notebooks/15-peering-facilities-ve.ipynb`: Expands on the analysis of Venezuela's presence at peering facilities.
- `./notebooks/16-chaos-txt-ve.ipynb`: Further investigates the presence of root DNS servers in Venezuela.
- `./notebooks/17-ripe-probe-count.ipynb`: Investigates the footprint of RIPE Atlas probes in Latin America.
- `./notebooks/19-third-party-providers-adoption.ipynb`: Analyzes the reliance on third-party providers by top sites across the LACNIC region.
- `./notebooks/20-google-dns-per-probe.ipynb`: Studies the per-probe latency to Google Public DNS resolvers.
- `./notebooks/notebook_utils.py`: Includes utility functions used across all notebooks.
