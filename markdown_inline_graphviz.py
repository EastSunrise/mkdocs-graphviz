"""
Graphviz extensions for Markdown.
Renders the output inline, eliminating the need to configure an output
directory.

Supports outputs types of SVG and PNG. The output will be taken from the
filename specified in the tag. Example:

{% dot attack_plan.svg
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
%}

Requires the graphviz library (http://www.graphviz.org/) and python 3

Inspired by jawher/markdown-dot (https://github.com/jawher/markdown-dot)
Forked from  cesaremorel/markdown-inline-graphviz (https://github.com/cesaremorel/markdown-inline-graphviz)

"""

import re
import markdown
import subprocess
import base64

# Global vars
BLOCK_RE_CURLY_BRACKET = re.compile(
        r'^{%[ ]* (?P<command>\w+)\s+(?P<filename>[^\s]+)\s*\n(?P<content>.*?)%}\s*$',
    re.MULTILINE | re.DOTALL)

BLOCK_RE_GRAVE_ACCENT = re.compile(
        r'^```graphviz[ ]* (?P<command>\w+)\s+(?P<filename>[^\s]+)\s*\n(?P<content>.*?)```\s*$',
    re.MULTILINE | re.DOTALL)

# Command whitelist
SUPPORTED_COMMAMDS = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']


class InlineGraphvizExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        """ Add InlineGraphvizPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        md.preprocessors.add('graphviz_block',
                             InlineGraphvizPreprocessor(md),
                             "_begin")


class InlineGraphvizPreprocessor(markdown.preprocessors.Preprocessor):

    def __init__(self, md):
        super(InlineGraphvizPreprocessor, self).__init__(md)

    def repair_svg_in_lines(self, lines):
        newLines = []
        searchText = "Generated by graphviz"
        for i in range(len(lines)):
            if i+3 <= len(lines)-1 and ( (searchText in lines[i+1]) or (searchText in lines[i+2]) or (searchText in lines[i+3]) ) :
                continue
            if i>=3 and ("<svg" in lines[i-1] and "Generated by graphviz" in lines[i-4]):
                continue
            if i>=3 and ("<svg" in lines[i] and "Generated by graphviz" in lines[i-3]):
                newLines.append(lines[i]+lines[i+1])
            else:
                newLines.append(lines[i])
        return newLines

    # def repair_svg_in_text(self, text):
    #     lines = text.split("\n")
    #     lines = self.repair_svg_in_lines(lines)
    #     return "".join(lines)


    def run(self, lines):
        """ Match and generate dot code blocks."""

        text = "\n".join(lines)
        while 1:
            m = BLOCK_RE_CURLY_BRACKET.search(text) if BLOCK_RE_CURLY_BRACKET.search(text) else BLOCK_RE_GRAVE_ACCENT.search(text)
            if not m:
                break
            else:
            # if m:
                command = m.group('command')
                # Whitelist command, prevent command injection.
                if command not in SUPPORTED_COMMAMDS:
                    raise Exception('Command not supported: %s' % command)
                filename = m.group('filename')
                content = m.group('content')
                filetype = filename[filename.rfind('.')+1:]

                args = [command, '-T'+filetype]
                try:
                    proc = subprocess.Popen(
                        args,
                        stdin=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        stdout=subprocess.PIPE)
                    proc.stdin.write(content.encode('utf-8'))

                    output, err = proc.communicate()

                    if filetype == 'svg':
                        encoding='utf-8'
                        output = output.decode(encoding)
                        outputLines = output.split("\n")
                        outputLines = self.repair_svg_in_lines(outputLines)
                        output = "\n".join(outputLines)
                        xmlHeaders = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n"""
                        output = xmlHeaders + output
                        
                        print("AVANT : TYPE(OUTPUT) = ", type(output))
                        encoding = 'base64'
                        output = output.encode('utf-8')
                        output = base64.b64encode(output).decode('utf-8')
                        print("APRES : TYPE(OUTPUT) = ", type(output))


                        data_url_filetype = 'svg+xml'
                        data_path = "data:image/%s;%s,%s" % (
                            data_url_filetype,
                            encoding,
                            output)
                        img = "![" + filename + "](" + data_path + ")"
                        # img = output
                        # output = output.encode('utf-8')
                        # img = output.decode('utf-8')
                        # the_encoding = chardet.detect(output)['encoding']
                        # print("the_encoding=", the_encoding)

                        # data_url_filetype = 'svg+xml'
                        # encoding='utf-8'
                        # img = output.decode('utf-8')

                    if filetype == 'png':
                        data_url_filetype = 'png'
                        encoding = 'base64'
                        output = base64.b64encode(output).decode('utf-8')
                        data_path = "data:image/%s;%s,%s" % (
                            data_url_filetype,
                            encoding,
                            output)
                        img = "![" + filename + "](" + data_path + ")"

                    text = '%s\n%s\n%s' % (
                        text[:m.start()], img, text[m.end():])
                    print("TEXT=", text)

                except Exception as e:
                        err = str(e) + ' : ' + str(args)
                        return (
                            '<pre>Error : ' + err + '</pre>'
                            '<pre>' + content + '</pre>').split('\n')

            # else:
            #     break
        # lines = text.split("\n")
        # lines = self.repair_svg_in_lines(lines)
        # print("LINES FINAL=", lines)
        # return lines
        return text.split("\n")


def makeExtension(*args, **kwargs):
    return InlineGraphvizExtension(*args, **kwargs)
