LOG_QUERIES = False
LOG_NOT_FOUND = False
EXTRA_FIELDS = [
    {'key': 'citycode'},
]
FILTERS = ['type', 'postcode', 'citycode', 'city']
BLOCKED_PLUGINS = ['addok.pairs', 'addok.fuzzy', 'addok.autocomplete']
QUERY_PROCESSORS = [
    'addok_france.extract_address',
    'addok_france.clean_query',
    'addok_france.glue_ordinal',
    'addok_france.fold_ordinal',
]
HOUSENUMBER_PROCESSORS = [
    'addok_france.glue_ordinal',
    'addok_france.fold_ordinal',
]
PROCESSORS = [
    'addok.helpers.text.tokenize',
    'addok.helpers.text.normalize',
    'addok.helpers.text.synonymize',
    'addok_fr.phonemicize',
    'addok_trigrams.trigramize',
]
RESULTS_COLLECTORS = [
    'addok.helpers.collectors.only_commons',
    'addok.helpers.collectors.bucket_with_meaningful',
    'addok.helpers.collectors.reduce_with_other_commons',
    'addok.helpers.collectors.ensure_geohash_results_are_included_if_center_is_given',  # noqa
    'addok_trigrams.extend_results_removing_numbers',
    'addok_trigrams.extend_results_removing_one_whole_word',
    'addok_trigrams.extend_results_removing_successive_trigrams',
]
SEARCH_RESULT_PROCESSORS = [
    'addok_trigrams.match_housenumber',
    'addok_france.make_labels',
    'addok.helpers.results.score_by_importance',
    'addok.helpers.results.score_by_autocomplete_distance',
    'addok.helpers.results.score_by_ngram_distance',
    'addok.helpers.results.score_by_geo_distance',
]
