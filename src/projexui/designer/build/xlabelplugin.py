#!/usr/bin/python

''' Auto-generated ui widget plugin '''

from projexui.qt.QtDesigner import QPyDesignerCustomWidgetPlugin
from projexui.qt.QtGui import QIcon

import projex.resources
from projexui.widgets.xlabel import XLabel as Base
setattr(Base, '__designer_mode__', True)

DEFAULT_XML = '''<ui language="c++" displayname="XLabel">
  <widget class="XLabel" name="XLabel"/>
  <customwidgets>
    <customwidget>
      <class>XLabel</class>
      <header>projexui.widgets.xlabel</header>
      <addpagemethod>%(addpagemethod)s</addpagemethod>
      <propertyspecifications>
        %(propertyspecs)s
      </propertyspecifications>
    </customwidget>
  </customwidgets>
</ui>'''

class XLabelPlugin(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent=None):
        super(XLabelPlugin, self).__init__(parent)
        
        self.initialized = False
    
    def initialize(self, core):
        if self.initialized:
            return
        
        self.initialized = True
    
    def isInitialized(self):
        return self.initialized
    
    def createWidget(self, parent):
        return Base(parent)
    
    def name(self):
        return getattr(Base, '__designer_name__', Base.__name__)
    
    def group(self):
        return getattr(Base, '__designer_group__', 'ProjexUI')
    
    def icon(self):
        default = projex.resources.find('img/logo_16.png')
        return QIcon(getattr(Base, '__designer_icon__', default))
    
    def toolTip( self ):
        docs = getattr(Base, '__doc__', '')
        if docs is None:
            docs = ''
        return getattr(Base, '__designer_tooltip__', docs)
    
    def whatsThis( self ):
        return ''
    
    def isContainer( self ):
        return getattr(Base, '__designer_container__', False)
    
    def includeFile( self ):
        return 'projexui.widgets.xlabel'
    
    def domXml( self ):
        opts = {}
        specs = []
        
        for prop, info in getattr(Base, '__designer_propspecs__', {}).items():
            xml  = '<%spropertyspecification name="%s" type="%s"/>'
            xml %= (info[0], prop, info[1])
            specs.append(xml)
        
        opts['addpagemethod'] = getattr(Base, '__designer_addpage__', '')
        opts['propertyspecs'] = ''.join(specs)
        default = DEFAULT_XML % opts
        return getattr(Base, '__designer_xml__', default)
