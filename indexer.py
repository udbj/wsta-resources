import sys, os, lucene, threading, time
from datetime import datetime
import glob
from java.io import File
from java.nio.file import Paths
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType,TextField
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version
from org.apache.lucene.analysis.cjk import CJKAnalyzer


lucene.initVM()
DIRTOINDX = 'wiki'
INDEXDIR = Paths.get('index')
indexdir = SimpleFSDirectory(INDEXDIR)

# analyzer = tokenizer
analyzer = CJKAnalyzer()

config = IndexWriterConfig(analyzer)

index_writer = IndexWriter(indexdir, config)

for filename in os.listdir(DIRTOINDX):
	filepath = os.path.join(DIRTOINDX, filename)

	document = Document()
	content = open(filepath, 'r').read()
	document.add(Field("file", filename, TextField.TYPE_STORED))
	document.add(Field("text", content, TextField.TYPE_STORED))

	index_writer.addDocument(document)

index_writer.commit()
index_writer.close()




 	


