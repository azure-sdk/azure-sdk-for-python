# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import Any, List, Union, overload
from ._operations import ContentSafetyClientOperationsMixin as ContentSafetyClientOperationsMixinGenerated
from .. import models as _models

__all__: List[str] = [
    "ContentSafetyClientOperationsMixin"
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """


class ContentSafetyClientOperationsMixin(ContentSafetyClientOperationsMixinGenerated):
    @overload
    def analyze_text(
        self, body: str, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AnalyzeTextResult:
        """Analyze Text.

        A synchronous API for the analysis of potentially harmful text content. Currently, it supports
        four categories: Hate, SelfHarm, Sexual, and Violence.

        parameter body: The text analysis request. Required.
        type body: string
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        parameter content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: AnalyzeTextResult. The AnalyzeTextResult is compatible with MutableMapping
        :rtype: ~azure.ai.contentsafety.models.AnalyzeTextResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        ...

    def analyze_text(self, body: str, **kwargs: Any) -> _models.AnalyzeTextResult:
        options = _models.AnalyzeTextOptions(text=body)
        return super().analyze_text(body=options, **kwargs)

    @overload
    def analyze_image(
        self, blob_url: str, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AnalyzeImageResult:
        """Analyze Image.

        A synchronous API for the analysis of potentially harmful image content. Currently, it supports
        four categories: Hate, SelfHarm, Sexual, and Violence.

        :param blob_url: The blob url of the image. Required.
        :type blob_url: string
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: AnalyzeImageResult. The AnalyzeImageResult is compatible with MutableMapping
        :rtype: ~azure.ai.contentsafety.models.AnalyzeImageResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def analyze_image(
        self, image_content: bytes, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.AnalyzeImageResult:
        """Analyze Image.

        A synchronous API for the analysis of potentially harmful image content. Currently, it supports
        four categories: Hate, SelfHarm, Sexual, and Violence.

        :param image_content: The Base64 encoding of the image. Required.
        :type image_content: bytes
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: AnalyzeImageResult. The AnalyzeImageResult is compatible with MutableMapping
        :rtype: ~azure.ai.contentsafety.models.AnalyzeImageResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    def analyze_image(self, data: Union[str, bytes], **kwargs: Any) -> _models.AnalyzeImageResult:
        _image = None
        if isinstance(data, bytes):
            _image = _models.ImageData(content=data)
        else:
            _image = _models.ImageData(blob_url=data)
        options = _models.AnalyzeImageOptions(image=_image)
        return super().analyze_image(body=options, **kwargs)
