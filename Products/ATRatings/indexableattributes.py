"""\
Prepare indexable attributes for the catalog. We do not add them by default 
to not slow down a site. Use them only in your catalog if you need them!
"""

from zope.interface import Interface

from Products.CMFCore.utils import getToolByName
#from Products.CMFPlone.CatalogTool import registerIndexableAttribute
from Products.Archetypes.interfaces import IReferenceable
from plone.indexer.decorator import indexer

@indexer(Interface)
def getHitCount(obj, portal, **kw):
    if not IReferenceable.providedBy(obj):
        return None
    rt = getToolByName(obj, 'portal_ratings')    
    return rt.getHitCount(obj.UID())

@indexer(Interface)
def getRatingCount(obj, portal, **kw):
    if not IReferenceable.providedBy(obj):
        return None
    rt = getToolByName(obj, 'portal_ratings')    
    return rt.getRatingCount(obj.UID())

@indexer(Interface)
def getRatingSum(obj, portal, **kw):
    if not IReferenceable.providedBy(obj):
        return None
    rt = getToolByName(obj, 'portal_ratings')    
    return rt.getRatingSum(obj.UID())

@indexer(Interface)
def getRatingSumSquared(obj, portal, **kw):
    if not IReferenceable.providedBy(obj):
        return None
    rt = getToolByName(obj, 'portal_ratings')    
    return rt.getRatingSumSquared(obj.UID())

@indexer(Interface)
def getRatingMean(obj, portal, **kw):
    if not IReferenceable.providedBy(obj):
        return None
    rt = getToolByName(obj, 'portal_ratings')    
    return rt.getRatingMean(obj.UID())

@indexer(Interface)
def getRatingStdDev(obj, portal, **kw):
    if not IReferenceable.providedBy(obj):
        return None
    rt = getToolByName(obj, 'portal_ratings')    
    return rt.getRatingStdDev(obj.UID())

@indexer(Interface)
def getRatingVariance(obj, portal, **kw):
    if not IReferenceable.providedBy(obj):
        return None
    rt = getToolByName(obj, 'portal_ratings')    
    return rt.getRatingSumSquared(obj.UID())

@indexer(Interface)
def getEstimatedRating(obj, portal, **kw):
    if not IReferenceable.providedBy(obj):
        return None
    rt = getToolByName(obj, 'portal_ratings')    
    return rt.getEstimatedRating(obj.UID())

@indexer(Interface)
def getCyninRating(obj, portal, **kw):
    if not IReferenceable.providedBy(obj):
        return None
    rt = getToolByName(obj, 'portal_ratings')    
    return rt.getCyninRating(obj.UID())
#
#registerIndexableAttribute("getRatingMean", getRatingMean)
#registerIndexableAttribute("getRatingSumSquared", getRatingSumSquared)
#registerIndexableAttribute("getRatingSum", getRatingSum)
#registerIndexableAttribute("getHitCount", getHitCount)
#registerIndexableAttribute("getRatingCount", getRatingCount)
#registerIndexableAttribute("getRatingStdDev", getRatingStdDev)
#registerIndexableAttribute("getRatingVariance", getRatingVariance)
#registerIndexableAttribute("getEstimatedRating", getEstimatedRating)
#registerIndexableAttribute("getCyninRating", getCyninRating)
