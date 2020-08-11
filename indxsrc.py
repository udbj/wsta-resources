import sys
import lucene
from java.io import File
from java.io import StringReader
from java.nio.file import Paths
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType,TextField
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig,IndexReader,DirectoryReader
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version
from org.apache.lucene.analysis.cjk import CJKAnalyzer
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.search.highlight import QueryScorer
from org.apache.lucene.search.highlight import SimpleHTMLFormatter
from org.apache.lucene.search.highlight import Highlighter
from org.apache.lucene.search.highlight import SimpleSpanFragmenter

lucene.initVM()

INDEXDIR = 'index'
indir = Paths.get(INDEXDIR)
indir = SimpleFSDirectory(indir)
indir = DirectoryReader.open(indir)

lucene_analyzer= CJKAnalyzer()
lucene_searcher= IndexSearcher(indir)

src = sys.argv[1]
query = QueryParser(src,lucene_analyzer).parse(src)
 
HighlightFormatter = SimpleHTMLFormatter();
query_score = QueryScorer (query)

highlighter = Highlighter(HighlightFormatter, query_score)

fragmenter  = SimpleSpanFragmenter(query_score, 64);
highlighter.setTextFragmenter(fragmenter); 


MAX = 10
total_hits =lucene_searcher.search(query, MAX)

print('Hits: ', len(total_hits.scoreDocs))
for hit in total_hits.scoreDocs:
	hdoc = lucene_searcher.doc(hit.doc)

	text = hdoc.get('text')
	ts = lucene_analyzer.tokenStream('text', StringReader(text))
	print('Doc: ', hdoc.get('file'), ' Score: ', hit.score, ' Text: ', highlighter.getBestFragments(ts, text, 3, "...")
 )



