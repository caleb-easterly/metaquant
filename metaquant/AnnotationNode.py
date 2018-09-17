import numpy as np


class AnnotationNode:
    def __init__(self, id, intensity):
        """
        :param id: unique id for the term
        :param intensity: a list with intensity for each sample.
        The order will be kept constant by referring to the SampleGroups() object when calling this.
        """
        self.id = id
        self.intensity = intensity
        self.npeptide = 1

        # the next three attributes are updated later in AnnotationHierarchy
        self.sample_children = None
        self.n_sample_children = None
        self.aggregated_intensity = None

    def add_peptide(self, intensity):
        self.intensity += intensity
        if intensity > 0:
            self.npeptide += 1



