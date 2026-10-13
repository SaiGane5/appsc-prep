import React, { useEffect } from 'react';
import { X, ExternalLink, ZoomIn } from 'lucide-react';

export default function ImageModal({ image, onClose }) {
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [onClose]);

  if (!image) return null;

  return (
    <div 
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/85 backdrop-blur-sm animate-fade-in"
      onClick={onClose}
    >
      <div 
        className="relative max-w-5xl w-full bg-[#181920] border border-[#343644] rounded-xl overflow-hidden shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between px-5 py-3.5 bg-[#20222c] border-b border-[#343644]">
          <span className="text-sm font-medium text-slate-300 truncate max-w-xl">
            {image.caption || image.alt_text || 'Image Viewer'}
          </span>
          <div className="flex items-center gap-2">
            <a 
              href={image.url} 
              target="_blank" 
              rel="noopener noreferrer"
              className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-700/50 transition-colors"
              title="Open full image in new tab"
            >
              <ExternalLink size={18} />
            </a>
            <button 
              onClick={onClose}
              className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-700/50 transition-colors"
            >
              <X size={20} />
            </button>
          </div>
        </div>

        <div className="p-3 bg-[#0d0e12] flex items-center justify-center min-h-[300px] max-h-[75vh] overflow-auto">
          <img 
            src={image.url} 
            alt={image.alt_text || 'Illustration'} 
            className="max-h-[70vh] w-auto max-w-full object-contain rounded-md"
          />
        </div>

        {image.caption && (
          <div className="px-5 py-3.5 bg-[#20222c] border-t border-[#343644] text-sm text-slate-300 leading-relaxed">
            <span className="font-semibold text-cyan-400">Caption: </span>
            {image.caption}
          </div>
        )}
      </div>
    </div>
  );
}
