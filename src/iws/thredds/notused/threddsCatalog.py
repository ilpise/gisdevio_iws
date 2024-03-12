## Harvesting
#
from functools import lru_cache
from thredds_crawler.crawl import Crawl

from owslib.map import wms111, wms130


@lru_cache()
def ThreddsCatalog(url,
                   version='1.3.0',
                   xml=None,
                   username=None,
                   password=None,
                   parse_remote_metadata=False,
                   timeout=30,
                   headers=None):
    """
    API for Web Map Service (WMS) methods and metadata.
    """
    '''wms factory function, returns a version specific WebMapService object

    @type url: string
    @param url: url of WFS capabilities document
    @type xml: string
    @param xml: elementtree object
    @type parse_remote_metadata: boolean
    @param parse_remote_metadata: whether to fully process MetadataURL elements
    @param timeout: time (in seconds) after which requests should timeout
    @return: initialized WebFeatureService_2_0_0 object
    '''

    print('TMES DTASETS')
    print(url)
    c = Crawl('https://iws.ismar.cnr.it/thredds/catalog.xml', select=[".*tmes"],
              skip=[".*collection", ".*history"],
              # debug=True
              )

    # c = Crawl('http://tds.maracoos.org/thredds/MODIS.xml', select=[".*-Agg"])
    print(c.datasets)

    return c.datasets



    # clean_url = 'https://iws.ismar.cnr.it/thredds/wms/tmes/TMES_waves_20221202.nc'
    # base_ows_url = clean_url
    #
    # if version in ['1.1.1']:
    #     return (
    #         base_ows_url,
    #         wms111.WebMapService_1_1_1(
    #             clean_url, version=version, xml=xml,
    #             parse_remote_metadata=parse_remote_metadata,
    #             username=username, password=password,
    #             timeout=timeout, headers=headers
    #         )
    #     )
    # elif version in ['1.3.0']:
    #     return (
    #         base_ows_url,
    #         wms130.WebMapService_1_3_0(
    #             clean_url, version=version, xml=xml,
    #             parse_remote_metadata=parse_remote_metadata,
    #             username=username, password=password,
    #             timeout=timeout, headers=headers
    #         )
    #     )
    # raise NotImplementedError(
    #     f'The WMS version ({version}) you requested is not implemented. Please use 1.1.1 or 1.3.0.')
