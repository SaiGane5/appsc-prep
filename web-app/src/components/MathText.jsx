import React from 'react';
import katex from 'katex';

export default function MathText({ text, className = '' }) {
  if (text === null || text === undefined) return null;
  if (typeof text !== 'string') return <span className={className}>{String(text)}</span>;

  // Quick return if string does not contain any LaTeX delimiters
  if (!text.includes('$') && !text.includes('\\(') && !text.includes('\\[')) {
    return <span className={className}>{text}</span>;
  }

  const parts = [];
  // Match $$...$$ or $...$ or \[...\] or \(...\)
  const regex = /(\$\$[\s\S]+?\$\$|\$[^\$\n]+?\$|\\\[[\s\S]+?\\\]|\\\([^\n]+?\\\))/g;
  let lastIdx = 0;
  let match;

  while ((match = regex.exec(text)) !== null) {
    if (match.index > lastIdx) {
      parts.push({
        type: 'text',
        content: text.slice(lastIdx, match.index)
      });
    }

    const raw = match[0];
    const isBlock = raw.startsWith('$$') || raw.startsWith('\\[');
    let math = raw;
    if (raw.startsWith('$$') && raw.endsWith('$$')) math = raw.slice(2, -2);
    else if (raw.startsWith('$') && raw.endsWith('$')) math = raw.slice(1, -1);
    else if (raw.startsWith('\\[') && raw.endsWith('\\]')) math = raw.slice(2, -2);
    else if (raw.startsWith('\\(') && raw.endsWith('\\)')) math = raw.slice(2, -2);

    try {
      const html = katex.renderToString(math.trim(), {
        displayMode: isBlock,
        throwOnError: false
      });
      parts.push({ type: 'math', html, isBlock });
    } catch {
      parts.push({ type: 'text', content: raw });
    }

    lastIdx = regex.lastIndex;
  }

  if (lastIdx < text.length) {
    parts.push({ type: 'text', content: text.slice(lastIdx) });
  }

  return (
    <span className={className}>
      {parts.map((p, i) => {
        if (p.type === 'math') {
          return (
            <span
              key={i}
              className={p.isBlock ? "block my-2 text-center" : "inline-block mx-0.5 align-baseline"}
              dangerouslySetInnerHTML={{ __html: p.html }}
            />
          );
        }
        return <span key={i}>{p.content}</span>;
      })}
    </span>
  );
}
